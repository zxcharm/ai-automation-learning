import json

with open("requests.json", "r", encoding="utf-8") as f:
    data = json.load(f)

urgent = []

for item in data:
    text = item["text"].lower()
    if "срочно" in text:
        urgent.append(item)

with open("urgent.json", "w", encoding="utf-8") as f:
    json.dump(urgent, f, ensure_ascii=False, indent=2)

print("Найдено срочных заявок: ", len(urgent))

import os
print(os.getcwd())