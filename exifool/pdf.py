from exifool.extractor import Extractor, close_file
from pypdf import PdfReader


class Pdf(Extractor):
    """
    Pdf is a class that enables retrieval of PDF metadata.
    """

    @close_file
    def get_metadata(self) -> dict:
        reader = PdfReader(self.file)
        return reader.metadata
