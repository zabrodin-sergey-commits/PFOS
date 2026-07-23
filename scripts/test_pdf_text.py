import fitz
import sys
from pathlib import Path


def main():

    if len(sys.argv) < 2:
        print("Использование:")
        print("py -m scripts.test_pdf_text <путь_к_pdf>")
        return

    file = Path(sys.argv[1])

    if not file.exists():
        print("Файл не найден:")
        print(file)
        return

    pdf = fitz.open(file)

    text = ""

    for page in pdf:
        text += page.get_text()

    pdf.close()

    Path("reports").mkdir(exist_ok=True)

    with open(
        "reports/pdf_text_utf8.txt",
        "w",
        encoding="utf-8"
    ) as f:
        f.write(text)

    print("Готово.")
    print("Файл сохранён:")
    print("reports/pdf_text_utf8.txt")


if __name__ == "__main__":
    main()