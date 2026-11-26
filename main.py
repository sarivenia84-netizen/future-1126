import os

output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
text = "Text from 2054: we solved fusion, aging and traffic. You still can't parallel park. The group chat is just condolences now. Water the plant."

os.makedirs(output_dir, exist_ok=True)
with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(text)
