import os
import logging
from collections import namedtuple

# Настройка логирования
logging.basicConfig(filename='directory_info.log', level=logging.INFO)

# Создание namedtuple для хранения информации о содержимом
FileInfo = namedtuple('FileInfo', ['name', 'extension', 'is_directory', 'parent_dir'])

def process_directory(directory_path):
    for item in os.listdir(directory_path):
        full_path = os.path.join(directory_path, item)
        is_directory = os.path.isdir(full_path)
        
        if is_directory:
            name = item
            extension = None
        else:
            name, extension = os.path.splitext(item)

        parent_dir = os.path.basename(directory_path)
        file_info = FileInfo(name=name, extension=extension, is_directory=is_directory, parent_dir=parent_dir)

        logging.info(f"Processed: {file_info}")

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python script.py <directory_path>")
    else:
        directory_path = sys.argv[1]
        if not os.path.exists(directory_path):
            print("Directory does not exist.")
        else:
            process_directory(directory_path)