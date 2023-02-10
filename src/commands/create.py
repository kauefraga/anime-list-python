import click
import validators
import datetime
from rich import print
from components.icons import Icon
from infra.db import Anime, db

@click.command()
@click.argument('title')
@click.argument('url')
def create(title: str, url: str):
  """Create an anime with a given title/description"""
  if not validators.url(url):
    print('{} [bold red]The URL is not valid'.format(Icon.MINUS.value))
    exit(0)

  animeAlreadyExists = Anime.get_or_none(Anime.title == title)

  if animeAlreadyExists:
    print('{} [bold red]{} already exists.'.format(Icon.MINUS.value, title))
    print('[red]Exiting...')
    exit(0)

  print('{} Title: [orange_red1]{}'.format(Icon.PLUS.value, title))
  print('{} URL: [orange_red1]{}'.format(Icon.PLUS.value, url))

  Anime.create(title=title, url=url, created_at=datetime.datetime.now())

  print('[green]Done!')
  print(f'[green]The anime {title} has been created in the database')

  db.close()
