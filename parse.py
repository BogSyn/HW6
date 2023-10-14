import sys
from pathlib import Path


JPEG_list = []
PNG_list = []
JPG_list = []
SVG_list = []

AVI_list = []
MP4_list = []
MOV_list = []
MKV_list = []

DOC_list = []
DOCX_list = []
TXT_list = []
PDF_list = []
XLSX_list = []
PPTX_list = []

MP3_list = []
OGG_list = []
WAV_list = []
AMR_list = []

ZIP_list = []
GZ_list = []
TAR_list = []

UNKNOWN_EXTENSIONS = []

REGISTER_EXTENSION = {
    'JPEG': JPEG_list,
    'PNG': PNG_list,
    'JPG': JPG_list,
    'SVG': SVG_list,
    'AVI': AVI_list,
    'MP4': MP4_list,
    'MOV': MOV_list,
    'MKV': MKV_list,
    'DOC': DOC_list,
    'DOCX': DOCX_list,
    'TXT': TXT_list,
    'PDF': PDF_list,
    'XLSX': XLSX_list,
    'PPTX': PPTX_list,
    'MP3': MP3_list,
    'OGG': OGG_list,
    'WAV': WAV_list,
    'AMR': AMR_list,
    'ZIP': ZIP_list,
    'GZ': GZ_list,
    'TAR': TAR_list,
}

FOLDERS = []
EXTENSIONS = set()
UNKNOWN = set()

# Витягуємо розширення, зрізаємо "." та переводимо у верхній регістр.


def get_extension(name: str) -> str:
    return Path(name).suffix[1:].upper()

# Робота з папками.


def scan(folder: Path):
    for item in folder.iterdir():                 # Ітеруємось по директорії.
        if item.is_dir():
            # Визначаємо папки, які пропускаємо
            if item.name not in ('images', 'documents', 'audio', 'video', 'archives', 'unknown_extension'):
                # Добавляємо в список всі шляхи до папок, крім вийнятків.
                FOLDERS.append(item)
                scan(item)                        # Рекурсія
            continue

        extension = get_extension(item.name)
        full_name = folder / item.name            # Повний шлях до файлу.
        # Добавляємо до списку шлях файлу, якщо немає розширеня.
        if not extension:
            UNKNOWN_EXTENSIONS.append(full_name)
        else:
            try:
                # Наповнюємо список словника файлами (повний шлях)
                take_from_dict = REGISTER_EXTENSION[extension]
                take_from_dict.append(full_name)
                # Добавляємо розширення (верзній регістр) до сету
                EXTENSIONS.add(extension)
            except KeyError:
                # Добавляємо до сету розширення, якщо невідоме.
                UNKNOWN.add(extension)
                # Добавляємо до списку шлях файлу, якщо невідоме розширеня.
                UNKNOWN_EXTENSIONS.append(full_name)


if __name__ == '__main__':
    folder_process = sys.argv[1]
    scan(Path(folder_process))
