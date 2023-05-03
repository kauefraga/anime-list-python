import click
from commands.list import list
from commands.create import create
from commands.find import find
from commands.save import save
from commands.status import status


@click.version_option('1.8.1', message='v%(version)s')
@click.group(context_settings={'help_option_names': ['-h', '--help']})
def cli():
  """
    📖 A list to save information about some animes\n
      example: python src/main.py list
  """
  pass

if __name__ == '__main__':
  cli.add_command(list)
  cli.add_command(create)
  cli.add_command(find)
  cli.add_command(save)
  cli.add_command(status)
  cli()
