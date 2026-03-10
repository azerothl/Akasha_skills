#!/usr/bin/env python3
"""
Generate synthetic dataset for Akasha synthetic-dataset skill.
Two modes:
  - Schema (Faker): --schema <path|->, --rows, --format, --output, --locale
  - Hugging Face: --from-hf <dataset_id>, --hf-split, --hf-config, --hf-columns, --rows, --format, --output
Output: CSV, JSON, or JSONL. MAX_ROWS applies to both modes.
"""
import argparse
import csv
import json
import random
import sys
from pathlib import Path

MAX_ROWS = 50_000

FAKER_TYPES = {
    "uuid": "uuid4",
    "name": "name",
    "first_name": "first_name",
    "last_name": "last_name",
    "email": "email",
    "phone": "phone_number",
    "address": "address",
    "city": "city",
    "country": "country",
    "company": "company",
    "job": "job",
    "date": "date",
    "date_time": "date_time",
    "iso8601": "iso8601",
    "integer": "random_int",
    "float": "pyfloat",
    "boolean": "boolean",
    "word": "word",
    "sentence": "sentence",
    "text": "text",
    "choice": "choice",
}


def load_schema(path: str) -> list:
    if path == "-":
        data = json.load(sys.stdin)
    else:
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
    if not isinstance(data, list):
        raise ValueError("Schema must be a JSON array of column definitions")
    for col in data:
        if not isinstance(col, dict) or "name" not in col or "type" not in col:
            raise ValueError("Each column must have 'name' and 'type'")
    return data


def generate_row_faker(schema: list, fake) -> dict:
    row = {}
    for col in schema:
        name = col["name"]
        typ = col["type"]
        if typ == "choice":
            values = col.get("values")
            if not values:
                raise ValueError(f"Column {name} type 'choice' requires 'values' list")
            row[name] = random.choice(values)
        elif typ == "integer":
            row[name] = fake.random_int(0, 999999)
        elif typ == "float":
            row[name] = round(fake.pyfloat(min_value=0, max_value=10000), 4)
        elif typ in FAKER_TYPES and FAKER_TYPES[typ] != "choice":
            method = FAKER_TYPES[typ]
            if method == "uuid4":
                import uuid
                row[name] = str(uuid.uuid4())
            else:
                row[name] = getattr(fake, method)()
        else:
            raise ValueError(f"Unknown schema type: {typ}")
    return row


def run_schema_mode(args) -> int:
    try:
        from faker import Faker
    except ImportError:
        print("Faker not installed. Run: pip install -r requirements.txt", file=sys.stderr)
        return 1
    schema = load_schema(args.schema)
    locale = args.locale or "en_US"
    fake = Faker(locale)
    rows = min(int(args.rows), MAX_ROWS)
    if rows <= 0:
        print("rows must be positive", file=sys.stderr)
        return 1
    out_path = args.output
    fmt = (args.format or "csv").lower()
    if fmt not in ("csv", "json", "jsonl"):
        print("format must be csv, json, or jsonl", file=sys.stderr)
        return 1

    def write_rows(writer):
        for _ in range(rows):
            row = generate_row_faker(schema, fake)
            writer(row)

    if fmt == "csv":
        columns = [c["name"] for c in schema]
        if out_path:
            with open(out_path, "w", newline="", encoding="utf-8") as f:
                w = csv.DictWriter(f, fieldnames=columns)
                w.writeheader()
                for _ in range(rows):
                    w.writerow(generate_row_faker(schema, fake))
        else:
            w = csv.DictWriter(sys.stdout, fieldnames=columns)
            w.writeheader()
            for _ in range(rows):
                w.writerow(generate_row_faker(schema, fake))
    elif fmt == "json":
        data = [generate_row_faker(schema, fake) for _ in range(rows)]
        if out_path:
            with open(out_path, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2, ensure_ascii=False, default=str)
        else:
            json.dump(data, sys.stdout, indent=2, ensure_ascii=False, default=str)
    else:  # jsonl
        if out_path:
            with open(out_path, "w", encoding="utf-8") as f:
                for _ in range(rows):
                    f.write(json.dumps(generate_row_faker(schema, fake), ensure_ascii=False, default=str) + "\n")
        else:
            for _ in range(rows):
                print(json.dumps(generate_row_faker(schema, fake), ensure_ascii=False, default=str))
    return 0


def run_hf_mode(args) -> int:
    try:
        from datasets import load_dataset
    except ImportError:
        print("datasets not installed. Run: pip install -r requirements.txt", file=sys.stderr)
        return 1
    dataset_id = args.from_hf
    split = args.hf_split or "train"
    config = args.hf_config or None
    columns = args.hf_columns.split(",") if args.hf_columns else None
    columns = [c.strip() for c in columns] if columns else None
    rows = min(int(args.rows), MAX_ROWS)
    if rows <= 0:
        print("rows must be positive", file=sys.stderr)
        return 1
    fmt = (args.format or "csv").lower()
    if fmt not in ("csv", "json", "jsonl"):
        print("format must be csv, json, or jsonl", file=sys.stderr)
        return 1
    out_path = args.output

    try:
        ds = load_dataset(dataset_id, config=config, split=split, trust_remote_code=True)
    except Exception as e:
        print(f"Failed to load dataset {dataset_id}: {e}", file=sys.stderr)
        return 1

    n_total = len(ds)
    if n_total == 0:
        print("Dataset is empty", file=sys.stderr)
        return 1
    indices = random.sample(range(n_total), min(rows, n_total)) if n_total > rows else list(range(n_total))
    subset = ds.select(indices)
    col_names = columns or subset.column_names

    if fmt == "csv":
        if out_path:
            with open(out_path, "w", newline="", encoding="utf-8") as f:
                w = csv.DictWriter(f, fieldnames=col_names, extrasaction="ignore")
                w.writeheader()
                for row in subset:
                    w.writerow({k: row.get(k) for k in col_names})
        else:
            w = csv.DictWriter(sys.stdout, fieldnames=col_names, extrasaction="ignore")
            w.writeheader()
            for row in subset:
                w.writerow({k: row.get(k) for k in col_names})
    elif fmt == "json":
        data = [dict(row) for row in subset]
        if out_path:
            with open(out_path, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2, ensure_ascii=False, default=str)
        else:
            json.dump(data, sys.stdout, indent=2, ensure_ascii=False, default=str)
    else:  # jsonl
        if out_path:
            with open(out_path, "w", encoding="utf-8") as f:
                for row in subset:
                    f.write(json.dumps(dict(row), ensure_ascii=False, default=str) + "\n")
        else:
            for row in subset:
                print(json.dumps(dict(row), ensure_ascii=False, default=str))
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description="Generate synthetic dataset (Faker schema or Hugging Face)")
    ap.add_argument("--schema", help="Path to schema JSON or - for stdin (schema mode)")
    ap.add_argument("--from-hf", help="Hugging Face dataset id (e.g. imdb, databricks/databricks-dolly-15k)")
    ap.add_argument("--hf-split", default="train", help="HF split: train, test, validation")
    ap.add_argument("--hf-config", help="HF config name")
    ap.add_argument("--hf-columns", help="Comma-separated columns to export (default: all)")
    ap.add_argument("--rows", type=int, default=100, help="Number of rows (default 100, max %d)" % MAX_ROWS)
    ap.add_argument("--format", choices=["csv", "json", "jsonl"], default="csv", help="Output format")
    ap.add_argument("--output", "-o", help="Output file path (default: stdout)")
    ap.add_argument("--locale", default="en_US", help="Faker locale (schema mode)")
    args = ap.parse_args()

    if args.from_hf:
        if args.schema:
            print("Cannot use --schema and --from-hf together", file=sys.stderr)
            return 1
        return run_hf_mode(args)
    if args.schema is None:
        print("Provide --schema or --from-hf", file=sys.stderr)
        return 1
    return run_schema_mode(args)


if __name__ == "__main__":
    sys.exit(main())
