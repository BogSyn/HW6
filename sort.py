from pathlib import Path
import parse
from normalize import normalize
import sys
import shutil

# Функція роботи з файлами.
# Створює цільовий каталог (якщо він не існує).
# Переносить нормалізований файл до відповідної папки.


def handle_files(file_name: Path, target_folder: Path):
    target_folder.mkdir(exist_ok=True, parents=True)
    file_name.replace(target_folder / normalize(file_name.name))

# Функція роботи з архівами.
# Створює цільовий каталог (якщо він не існує)
# Створює новий каталог для файлів, які були розпаковані з архіву.
# Ім'я цього каталогу базується на імені архіву,
# видаливши розширення файлу (.zip, .tar, тощо) і нормалізувавши його.


def handle_archive(file_name: Path, target_folder: Path):
    target_folder.mkdir(exist_ok=True, parents=True)
    folder_for_file = target_folder / \
        normalize(file_name.name.replace(file_name.suffix, ''))
    folder_for_file.mkdir(exist_ok=True, parents=True)
    try:  # Розпаковує архівний файл
        shutil.unpack_archive(str(file_name.absolute()),
                              str(folder_for_file.absolute()))
    except shutil.ReadError:  # Видаляє створений каталог і припиняє виконання функції
        folder_for_file.rmdir()
        return
    file_name.unlink()  # Видаляє архівний файл.


def main(folder: Path):
    parse.scan(folder)
    # Обробляє відомі розширення
    for file in parse.JPEG_list:
        handle_files(file, folder / 'images' / 'JPEG')
    for file in parse.PNG_list:
        handle_files(file, folder / 'images' / 'PNG')
    for file in parse.JPG_list:
        handle_files(file, folder / 'images' / 'JPG')
    for file in parse.SVG_list:
        handle_files(file, folder / 'images' / 'SVG')
    for file in parse.AVI_list:
        handle_files(file, folder / 'video' / 'AVI')
    for file in parse.MP4_list:
        handle_files(file, folder / 'video' / 'MP4')
    for file in parse.MOV_list:
        handle_files(file, folder / 'video' / 'MOV')
    for file in parse.MKV_list:
        handle_files(file, folder / 'video' / 'MKV')
    for file in parse.DOC_list:
        handle_files(file, folder / 'documents' / 'DOC')
    for file in parse.DOCX_list:
        handle_files(file, folder / 'documents' / 'DOCX')
    for file in parse.TXT_list:
        handle_files(file, folder / 'documents' / 'TXT')
    for file in parse.PDF_list:
        handle_files(file, folder / 'documents' / 'PDF')
    for file in parse.XLSX_list:
        handle_files(file, folder / 'documents' / 'XLSX')
    for file in parse.PPTX_list:
        handle_files(file, folder / 'documents' / 'PPTX')
    for file in parse.MP3_list:
        handle_files(file, folder / 'audio' / 'MP3')
    for file in parse.OGG_list:
        handle_files(file, folder / 'audio' / 'OGG')
    for file in parse.WAV_list:
        handle_files(file, folder / 'audio' / 'WAV')
    for file in parse.AMR_list:
        handle_files(file, folder / 'audio' / 'AMR')
    # Обробляє невідомі розширення
    for file in parse.UNKNOWN_EXTENSIONS:
        handle_files(file, folder / 'unknown_extension')
    # Обробляє відомі розширення архівів
    for file in parse.ZIP_list:
        handle_archive(file, folder / 'archives')
    for file in parse.GZ_list:
        handle_archive(file, folder / 'archives')
    for file in parse.TAR_list:
        handle_archive(file, folder / 'archives')

    # Видаляє кожен елемент зі списку зворотньому порядку.
    for folder in parse.FOLDERS[::-1]:
        try:
            folder.rmdir()
        except OSError:
            print(f'Error during remove folder {folder}')


if __name__ == "__main__":
    folder_process = Path(sys.argv[1])
    main(folder_process.resolve())

    print(f'EXTENSIONS: {list(parse.EXTENSIONS)}')
    print(f'UNKNOWN_EXTENSIONS: {list(parse.UNKNOWN)}')
