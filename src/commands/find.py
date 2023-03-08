import click
from rich import print

from components.icons import Icon
from infra.db import Anime, db

@click.command()
@click.argument('title', required=False)
def find(title: str):
  """Search for an anime with a title and return it with a url"""
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
