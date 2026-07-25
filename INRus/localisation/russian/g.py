import os
import glob

def remove_zero_suffix():
    # Находит все .yml файлы в текущей директории и поддиректориях
    yaml_files = glob.glob('**/*.yml', recursive=True)
    
    for file_path in yaml_files:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Заменяем ':0' на ':'
            new_content = content.replace(':0', ':')
            
            if content != new_content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Обновлен файл: {file_path}")
                
        except Exception as e:
            print(f"Ошибка при обработке файла {file_path}: {e}")

if __name__ == '__main__':
    remove_zero_suffix()
    print("Готово!")