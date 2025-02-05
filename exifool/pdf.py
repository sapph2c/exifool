from exifool.extractor import Extractor

class Pdf(Extractor):
    """
    Pdf is a class that enables retrieval of PDF metadata.
    """
    def __init__(self, file):
        self.file = file

    def get_metadata(self) -> list:
        pass
