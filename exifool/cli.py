from exifool.utility import get_extractor

import click
import rich


@click.command()
@click.option("--path", help="Path to the file to perform metadata analysis on.")
def cli(path: str):
    """
    \b
    ___________      .__  _____             .__
    \_   _____/__  __|__|/ ____\____   ____ |  |
    |     __)_\  \/  /  \   __\/  _ \ /  _ \|  |
    |         \>    <|  ||  | (  <_> |  <_> )  |__
    /_______  /__/\_ \__||__|  \____/ \____/|____/
            \/      \/

    Written with ❤️ by sapph2c

    Metadata analysis tool written for CSEC-473
    """

    extractor = get_extractor(path)
    metadata = extractor.get_metadata()
    rich.print(metadata)
