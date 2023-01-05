import click
from commands.list import list
from commands.save import save
from commands.open import open

@click.group()
def cli():
  pass

if __name__ == '__main__':
  cli.add_command(list)
  cli.add_command(save)
  cli.add_command(open)
  cli()
