import click
from commands.list import list
from commands.save import save
from commands.open import open

@click.version_option('1.5.0', message='%(prog)s version %(version)s')
@click.group(context_settings={'help_option_names': ['-h', '--help']})
def cli():
  """
    A list to save information about some animes\n
      example: python src/main.py list
  """
  pass

if __name__ == '__main__':
  cli.add_command(list)
  cli.add_command(save)
  cli.add_command(open)
  cli()
