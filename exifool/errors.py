class ExifoolError(Exception):
    """
    Base class for all exifool exceptions
    """

    def __init__(self, message, error_code):
        self.message = message
        self.error_code = error_code

    def __str__(self) -> str:
        return f"{self.message}, {self.error_code}"


class UnsupportedFiletype(ExifoolError):
    """
    Exception that's raised when an unsupported file type is encountered.
    """
