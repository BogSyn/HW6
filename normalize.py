import re

UA_SYMBOLS = 'абвгґдеєжзиіїйклмнопрстуфхцчшщьюя'
TRANSLITERATION = ("a", "b", "v", "h", "g", "d", "e", "ie", "zh", "z", "y", "i", "yi", "i", "k", "l", "m", "n", "o", "p", "r", "s",
                   "t", "u", "f", "kh", "ts", "ch", "sh", "shch", "", "yu", "ya")

TRANS_MAP = dict()

# Створюємо словник транслітерації.
for cyrillic, latin in zip(UA_SYMBOLS, TRANSLITERATION):
    TRANS_MAP[ord(cyrillic)] = latin
    TRANS_MAP[ord(cyrillic.upper())] = latin.upper()


def normalize(name: str) -> str:
    # Замінюємо будь-який символ крім цифри, букви та крапки на "_",  + робимо транслітерацію букв.
    translate_name = re.sub(r'[^\w\.]', '_', name.translate(TRANS_MAP))
    return translate_name


if __name__ == '__main__':

    print(len(UA_SYMBOLS))
    print(len(TRANSLITERATION))

    print(normalize('Mій файл_My file.docx'))
