from pathlib import Path
import importlib.util

MIGRATIONS_DIR = Path(__file__).parent / "migrations"


def run():

    print("=" * 50)
    print("PFOS DATABASE MIGRATIONS")
    print("=" * 50)

    migration_files = sorted(MIGRATIONS_DIR.glob("*.py"))

    for migration in migration_files:

        if migration.name.startswith("__"):
            continue

        print(f"\n>>> {migration.name}")

        spec = importlib.util.spec_from_file_location(
            migration.stem,
            migration
        )

        module = importlib.util.module_from_spec(spec)

        spec.loader.exec_module(module)

        if hasattr(module, "upgrade"):

            module.upgrade()

        else:

            print("Нет функции upgrade()")

    print("\nВсе миграции завершены.")


if __name__ == "__main__":
    run()