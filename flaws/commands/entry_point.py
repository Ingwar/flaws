import click

from .init import init
from .upload import upload
from .run import run


@click.group()
def flaws() -> None:
    pass


flaws.add_command(init)
flaws.add_command(upload)
flaws.add_command(run)
