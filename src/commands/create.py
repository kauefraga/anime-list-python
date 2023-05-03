import click
import datetime
from rich import print

from utils.validators import is_url
from components.icons import Icon
from infra.db import Anime, db


@click.command()
@click.argument('title')
@click.argument('url')
def create(title: str, url: str):
  """Create an anime with a given title/description"""
  if not is_url(url):
    print(f'{Icon.MINUS.value} [bold red]The URL is not valid')
    exit(0)

  print(f'{Icon.INTERROGATIVE.value} Checking if the anime already exists...')
  animeAlreadyExists = Anime.get_or_none(Anime.title == title)

  if animeAlreadyExists:
    print(f'{Icon.MINUS.value} [bold red]{title} already exists.')
    exit(0)

  print(f'{Icon.PLUS.value} Title: [orange_red1]{title}')
  print(f'{Icon.PLUS.value} URL: [orange_red1]{url}')

  Anime.create(title=title, url=url, created_at=datetime.datetime.now())

  print('[green]Done!')
  print(f'[green]The anime {title} has been created in the database')

  db.close()
