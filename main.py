from pathlib import Path
import sys

from scripts.pdf_handler import process_pdf


def main():

    print("=" * 40)
    print("PFOS Import Center")
    print("=" * 40)
    print()

    force = "--force" in sys.argv

    if force:
        print("Режим принудительного импорта включен")
        print()

    folder = Path("imports/vtb")

    if not folder.exists():

        print("Папка imports/vtb не найдена.")
        return


    for file in folder.iterdir():

        if file.is_file():

            process_pdf(
                file,
                force=force
            )


    print()
    print("Импорт завершен.")



if __name__ == "__main__":
    main()