import hashlib
import fitz

from import_center.detector import detect_parser
from import_center.document_builder import build_document

from analytics.categories import normalize_operation
from analytics.transfers import remove_internal_transfers
from analytics.text_normalizer import normalize_description

from database.repository import save_operations

from database.documents import (
    init_documents_table,
    document_exists,
    save_document
)


def create_document_id(file):

    with open(file, "rb") as f:
        data = f.read()

    return hashlib.md5(data).hexdigest()



def process_pdf(file, force=False):

    print("Тип файла : PDF")
    print(f"Имя файла : {file.name}")

    init_documents_table()

    document_id = create_document_id(file)


    if document_exists(document_id) and not force:

        print()
        print("Документ уже импортирован.")
        print("Импорт пропущен.")

        return


    pdf = fitz.open(file)

    text = ""

    for page in pdf:
        text += page.get_text()

    pdf.close()



    with open(
        "reports/last_import.txt",
        "w",
        encoding="utf-8"
    ) as report:

        report.write(text)



    document = build_document(text)


    parser = detect_parser(document.text)


    if parser is None:

        print()
        print("Парсер для документа не найден.")
        print("Импорт остановлен.")

        return



    statement = parser.parse(document)



    operations = statement.operations



    # --------------------------------------------------
    # Обработка обычных операций
    # --------------------------------------------------

    for operation in operations:

        operation.bank = statement.bank
        operation.account = statement.account
        operation.owner = statement.owner


        operation.description = normalize_description(
            operation.description
        )


        normalize_operation(operation)



    operations = remove_internal_transfers(
        operations
    )



    save_document(
        document_id,
        file.name,
        statement.bank
    )


    # Сохраняем операции только если они есть

    if operations:

        save_operations(
            operations,
            document_id
        )



    print()


    print(
        f"Внутренних переводов найдено: "
        f"{sum(1 for x in operations if getattr(x, 'internal_transfer', False))}"
    )



    print()

    print("===== Выписка =====")

    print(f"Банк       : {statement.bank}")
    print(f"Документ   : {statement.document_type}")
    print(f"Счет       : {statement.account}")
    print(f"Владелец   : {statement.owner}")



    # --------------------------------------------------
    # Вывод кредита
    # --------------------------------------------------

    if hasattr(statement, "loan"):

        print()
        print("===== КРЕДИТ =====")

        loan = statement.loan


        print(
            f"Тип        : {getattr(loan, 'loan_type', '')}"
        )

        print(
            f"Договор    : {getattr(loan, 'contract_number', '')}"
        )

        print(
            f"Остаток    : {getattr(loan, 'balance', 0)} RUB"
        )



        if hasattr(statement, "loan_summary"):

            print()

            print("Расчет:")


            for key, value in statement.loan_summary.items():

                print(
                    f"{key:20}: {value}"
                )



    print()

    print("===== Операции =====")


    for operation in operations[:10]:

        print(operation)



    print()

    print("Импорт завершен.")