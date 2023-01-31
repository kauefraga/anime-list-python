import click
from rich import print
from components.icons import Icon
from infra.db import Anime, db

WHITELIST = [
  'https://betteranime.net',
  'https://puray.moe',
  'https://animesonline.cc - https://animesonlinex.cx',
  'https://animestc.net',
  'https://animeszone.net',
]

@click.command()
@click.option('--all', '-a', is_flag=True, help='Show a list of nice websites')
@click.argument('title', required=False)
def find(all: bool, title: str):
  """Search for an anime with a title and return it with a url"""
  if all:
    for i in range(len(WHITELIST)):
      print('{} {}'.format(Icon.PLUS.value, WHITELIST[i]))
    exit(0)

  if title is None:
    print('{} No title provided'.format(Icon.MINUS.value))
    exit(0)

  print('{} Searching...'.format(Icon.INTERROGATIVE.value))

  anime = Anime.get_or_none(Anime.title.startswith(title))

  if anime is None:
    print('{} [bold red]{} not found. [/bold red]'.format(Icon.MINUS.value, title))
    exit(0)

  print('[bold green]Found![/bold green]')

  print('{} Title: [orange_red1]{}[/orange_red1]'.format(Icon.PLUS.value, anime.title))
  print('{} URL: [orange_red1]{}[/orange_red1]'.format(Icon.PLUS.value, anime.url))

  db.close()
