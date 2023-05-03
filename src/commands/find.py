import click
from rich import print

from components.icons import Icon
from infra.db import Anime, db


@click.command()
@click.argument('title', required=False)
def find(title: str):
  """Search for an anime with a title and return it with a url"""
  if title is None:
    print(f'{Icon.MINUS.value} [bold red]No title provided')
    exit(0)

  print(f'{Icon.INTERROGATIVE.value} Searching...')

  anime = Anime.get_or_none(Anime.title.startswith(title))

  if anime is None:
    print(f'{Icon.MINUS.value} [bold red]{title} not found.')
    exit(0)

  print('[bold green]Found!')

  print(f'{Icon.PLUS.value} Title: [orange_red1]{anime.title}')
  print(f'{Icon.PLUS.value} URL: [orange_red1]{anime.url}')

  db.close()
