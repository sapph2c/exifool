class Extractor:
    """
    Interface to be implemented by all metadata extractors.
    """
    def get_metadata(self) -> list:
        """
        Return all file metadata.
        """
        pass
