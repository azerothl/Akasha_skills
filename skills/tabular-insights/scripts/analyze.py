#!/usr/bin/env python3
"""DuckDB bridge for tabular-insights (until analyze_table native is default)."""
import sys

def main():
    if len(sys.argv) < 3:
        print("usage: analyze.py <inspect|summary|query> <path> [sql]", file=sys.stderr)
        sys.exit(1)
    action, path = sys.argv[1], sys.argv[2]
    sql = sys.argv[3] if len(sys.argv) > 3 else None
    try:
        import duckdb
    except ImportError:
        print("error: pip install duckdb openpyxl", file=sys.stderr)
        sys.exit(1)

    con = duckdb.connect()
    ext = path.lower().split(".")[-1]
    if ext in ("xlsx", "xls"):
        con.execute("INSTALL spreadsheet; LOAD spreadsheet;")
        con.execute("CREATE TABLE t AS SELECT * FROM read_xlsx(?)", [path])
    else:
        con.execute("CREATE TABLE t AS SELECT * FROM read_csv_auto(?)", [path])

    if action == "inspect":
        print(con.execute("DESCRIBE t").fetchdf().to_string())
        print("\nRow count:", con.execute("SELECT COUNT(*) FROM t").fetchone()[0])
    elif action == "summary":
        df = con.execute("SUMMARIZE t").fetchdf()
        print(df.to_string())
    elif action == "query":
        if not sql:
            print("query action requires SQL", file=sys.stderr)
            sys.exit(1)
        print(con.execute(sql).fetchdf().to_string())
    else:
        print("unknown action", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
