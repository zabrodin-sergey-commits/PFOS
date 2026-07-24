import fitz
from pathlib import Path

pdf = Path(r"imports/vtb/Выписка ВТБ по кредиту на авто.pdf")

txt = pdf.with_suffix(".txt")

doc = fitz.open(pdf)

with open(txt, "w", encoding="utf-8") as f:
    for page in doc:
        f.write(page.get_text())
        f.write("\n\n")

doc.close()

print(f"PDF : {pdf.resolve()}")
print(f"TXT : {txt.resolve()}")
print()
print("ГОТОВО")