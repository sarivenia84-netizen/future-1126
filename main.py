# MakeFun one-liner entry point
# =============================
# This script writes a predetermined entry line to an output directory.
# The entry text remains identical across all versions for bounty verification.
# Usage: MAKEFUN_OUTPUT_DIR=/path/to/output python3 main.py

ENTRY_LINE = "Text from 2054: we solved fusion, aging and traffic. You still can't parallel park. The group chat is just condolences now. Water the plant."

import os

output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
os.makedirs(output_dir, exist_ok=True)
with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(ENTRY_LINE)