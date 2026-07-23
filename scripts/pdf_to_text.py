from pathlib import Path
import fitz

ROOT = Path(__file__).resolve().parent.parent

pdf = ROOT / "imports" / "vtb" / "Выписка ВТБ по кредитной карте.pdf"
txt = ROOT / "imports" / "vtb" / "Выписка ВТБ по кредитной карте.txt"

print("PDF :", pdf)
print("TXT :", txt)

if not pdf.exists():
    print("ФАЙЛ НЕ НАЙДЕН!")
    raise SystemExit

doc = fitz.open(str(pdf))

with open(txt, "w", encoding="utf-8") as f:
    for page in doc:
        f.write(page.get_text())
        f.write("\n\n")

doc.close()

print("\nГОТОВО")
print(txt)