"""Writes one satirical sentence roasting lawmakers to /output/entry.txt."""
import os

TEXT = "Our lawmakers can write a 400-page bill to regulate artificial intelligence, but when the clerk asked for it as a PDF, the chairman printed it, scanned it, and emailed the scan as a JPEG."

# Rule: the roast must be a single sentence of 1 to 320 characters.
assert "\n" not in TEXT and TEXT.count(".") == 1 and TEXT.endswith(".") and 1 <= len(TEXT) <= 320, f"entry must be one sentence, 1-320 chars (got {len(TEXT)})"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(TEXT + "\n")
