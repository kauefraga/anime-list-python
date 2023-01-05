import click
from commands.list import list
from commands.save import save
from commands.open import open

@click.version_option('0.1.0', message='%(prog)s version %(version)s')
@click.group(context_settings={'help_option_names': ['-h', '--help']})
def cli():
  pass

if __name__ == '__main__':
  cli.add_command(list)
  cli.add_command(save)
  cli.add_command(open)
  cli()
