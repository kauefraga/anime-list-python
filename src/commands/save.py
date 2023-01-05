import click, validators, datetime
from rich import print
from infra.db import Anime, db

@click.command()
@click.argument('title')
@click.argument('url')
def save(title: str, url: str):
  if not validators.url(url):
    print('[bold red]The URL is not valid[/bold red]')

  print('Title: [orange_red1]{}[/orange_red1]'.format(title))
  print('URL: [orange_red1]{}[/orange_red1]'.format(url))

  Anime.create(title=title, url=url, created_at=datetime.datetime.now())

  print('[green]The anime {} is saved in the database[/green]'.format(title))

  db.close()
