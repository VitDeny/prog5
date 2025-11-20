import json

with open("people.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print("Дані з JSON файлу:\n")
for surname, info in data.items():
    print(f"{surname} {info[0]} {info[1]}, {info[2]} р.н.")
