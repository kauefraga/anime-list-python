import click
from commands.list import list
from commands.create import create
from commands.open import open
from commands.save import save

@click.version_option('1.6.0', message='%(prog)s version %(version)s')
@click.group(context_settings={'help_option_names': ['-h', '--help']})
def cli():
  """
    A list to save information about some animes\n
      example: python src/main.py list
  """
  pass

if __name__ == '__main__':
  cli.add_command(list)
  cli.add_command(create)
  cli.add_command(open)
  cli.add_command(save)
  cli()
