from pathlib import Path
from pdf_handler import process_pdf


def process_file(file):
    if file.suffix.lower() == ".pdf":
        process_pdf(file)
    else:
        print(f"Неизвестный тип файла: {file.name}")


print("=" * 40)
print("PFOS Import Center")
print("=" * 40)
print()

folder = Path("imports/vtb")

for file in folder.iterdir():
    if file.is_file():
        process_file(file)

print()
print("Импорт завершен.")