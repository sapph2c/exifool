from exifool.extractor import Extractor
from exifool.errors import UnsupportedFiletype
from exifool.pdf import Pdf

import pathlib


def get_extractor(path) -> Extractor:
    extension = get_file_extension(path)
    file = open(path, "rb")
    match extension:
        case "pdf":
            return Pdf(file)
        case _:
            raise UnsupportedFiletype(
                f"{extension} is not currently supported by exifool", 1
            )


def get_file_extension(path):
    return pathlib.Path(path).suffix[1:]
