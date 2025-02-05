from exifool.extractor import Extractor
from pypdf import PdfReader


class Pdf(Extractor):
    """
    Pdf is a class that enables retrieval of PDF metadata.
    """

    def __init__(self, file) -> None:
        self.reader = PdfReader(file)

    def get_metadata(self) -> list:
        return self.reader.metadata
