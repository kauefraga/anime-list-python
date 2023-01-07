import click, validators, datetime
from rich import print
from components.icons import Icon
from infra.db import Anime, db

@click.command()
@click.argument('title')
@click.argument('url')
def create(title: str, url: str):
  """Create an anime with a given title/description"""
  if not validators.url(url):
    print('{} [bold red]The URL is not valid[/bold red]'.format(Icon.MINUS.value))
    exit(0)

  animeAlreadyExists = Anime.get_or_none(Anime.title == title)

  if animeAlreadyExists:
    print('{} [bold red]{} already exists[/bold red]'.format(Icon.MINUS.value, title))
    exit(0)

  print('{} Title: [orange_red1]{}[/orange_red1]'.format(Icon.PLUS.value, title))
  print('{} URL: [orange_red1]{}[/orange_red1]'.format(Icon.PLUS.value, url))

  Anime.create(title=title, url=url, created_at=datetime.datetime.now())

  print('[green]Done![/green]')
  print('[green]The anime {} has been created in the database[/green]'.format(title))

  db.close()
