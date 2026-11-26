#!/usr/bin/env python3
"""Write the winning one-sentence apology to /output/entry.txt.

Tournament winner (38 candidates, head-to-head in both orders, 3 rounds, 7-0):
"I'm sorry I replied-all to your entire company with "noted, thanks" on the
email where you were venting about your entire company." (130 chars)
"""
import os

LINE = "I'm sorry I replied-all to your entire company with \"noted, thanks\" on the email where you were venting about your entire company."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    # Read-back verification: the gate requires 1-200 UTF-8 chars, one sentence.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    assert written == LINE, "entry.txt does not match the winning line"
    assert 1 <= len(written) <= 200, f"char count {len(written)} outside 1-200"
    assert written.count(".") == 1 and written.endswith("."), "must be one sentence"
    print(f"entry.txt OK: {len(written)} chars, one sentence")

if __name__ == "__main__":
    main()
