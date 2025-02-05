import click
import logging

logging.basicConfig(level=logging.INFO)

@click.command()
@click.argument("file")
@click.option(
    "--file",
    help="Path to the file to perform metadata analysis on."
)
def cli():
    pass
