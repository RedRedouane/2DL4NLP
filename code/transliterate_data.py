"""
Installation instructions:
> pip install transliterate
> pip install pythainlp

"""

import os
from pythainlp.transliterate import romanize
from transliterate import translit, get_available_language_codes


DATA_DIR = os.path.join("all_data")
OVERWRITE = True


def loop_the_data(dir=DATA_DIR, overwrite=OVERWRITE):
    filenames = set([filename for filename in os.listdir(dir)])
    for filename in filenames:
        i = filename.find(".r.")
        j = filename.rfind(".")
        lang = filename[j + 1:]
        if i == -1 and lang not in {"en", "tr"}:
            romanized_filename = filename[:j] + ".r" + filename[j:]
            if overwrite or romanized_filename not in filenames:
                print("transliterating", filename, "into", romanized_filename)
                with open(os.path.join(dir, filename), encoding="utf-8") as from_f,\
                     open(os.path.join(dir, romanized_filename), 'w', encoding="utf-8") as to_f:
                    romanize_data(from_f, to_f, filename[j + 1:])


def romanize_data(from_f, to_f, lang):

    if lang in get_available_language_codes():
        to_f.write(translit(from_f.read(), lang, reversed=True))
    elif lang == "th":
        to_f.write(romanize(from_f.read()))
    else:
        print("did not transliterate", lang)


loop_the_data(DATA_DIR)
