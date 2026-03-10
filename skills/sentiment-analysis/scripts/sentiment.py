#!/usr/bin/env python3
"""
Sentiment analysis script for Akasha sentiment-analysis skill.
Uses Hugging Face transformers pipeline; outputs JSON: {"label": "POSITIVE|NEGATIVE", "score": float}.
Input: first argument or stdin.
"""
import json
import sys

# Limit input length to avoid timeouts and model limits
MAX_INPUT_LEN = 512


def main() -> None:
    if len(sys.argv) > 1:
        text = " ".join(sys.argv[1:]).strip()
    else:
        text = sys.stdin.read().strip()

    if not text:
        print(json.dumps({"error": "No text provided", "label": None, "score": None}), file=sys.stderr)
        sys.exit(1)

    if len(text) > MAX_INPUT_LEN:
        text = text[:MAX_INPUT_LEN].rsplit(maxsplit=1)[0] or text[:MAX_INPUT_LEN]

    try:
        from transformers import pipeline
    except ImportError:
        out = {"error": "transformers not installed. Run: pip install -r requirements.txt", "label": None, "score": None}
        print(json.dumps(out))
        sys.exit(1)

    try:
        pipe = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
    except Exception as e:
        print(json.dumps({"error": str(e), "label": None, "score": None}))
        sys.exit(1)

    try:
        result = pipe(text)
        if result:
            r = result[0]
            label = r.get("label", "N/A")
            score = r.get("score", 0.0)
            print(json.dumps({"label": label, "score": round(score, 4)}))
        else:
            print(json.dumps({"label": None, "score": None, "error": "No result"}))
    except Exception as e:
        print(json.dumps({"error": str(e), "label": None, "score": None}))
        sys.exit(1)


if __name__ == "__main__":
    main()
