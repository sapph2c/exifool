import functools


class Extractor:
    """
    Extractor is an interface to be implemented by all metadata extractors.
    """

    def __init__(self, file):
        self.file = file

    def get_metadata(self) -> dict:
        """
        Return all file metadata.
        """
        return {}


def close_file(func):
    """
    close_file is a decorator used to ensure that the file is closed after get_metadata is ran.
    """

    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        try:
            return func(self, *args, **kwargs)
        finally:
            self.file.close()

    return wrapper
