from exifool.extractor import Extractor
from exifool.utility import get_extractor

import click
import rich


@click.command()
@click.option("--path", help="Path to the file to perform metadata analysis on.")
def cli(path: str):
    extractor = get_extractor(path)
    metadata = extractor.get_metadata()
    rich.print(metadata)
