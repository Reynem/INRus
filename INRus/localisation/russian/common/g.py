import os


def process_localization_files(root_dir="."):
    # Проходим по всем папкам и файлам
    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith(".yml"):
                old_file_path = os.path.join(dirpath, filename)

                # 1. Замена содержимого файла (:0 -> :)
                try:
                    with open(old_file_path, "r", encoding="utf-8-sig") as f:
                        content = f.read()

                    new_content = content.replace(":0", ":")

                    with open(old_file_path, "w", encoding="utf-8") as f:
                        f.write(new_content)
                except Exception as e:
                    print(
                        f"Ошибка при чтении/записи файла {old_file_path}: {e}"
                    )
                    continue

if __name__ == "__main__":
    print("Запуск обработки yml-файлов...")
    process_localization_files()
    print("Готово!")