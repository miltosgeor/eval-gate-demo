import json, sys
from app import classify

cases = json.load(open("golden.json"))
passed = sum(classify(c["input"]) == c["expected"] for c in cases)
score = passed / len(cases)
print(f"Eval score: {score:.0%} ({passed}/{len(cases)})")

if score < 0.9:   # the quality gate threshold
    sys.exit(1)   # a non-zero exit fails the pipeline