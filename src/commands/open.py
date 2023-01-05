import click
from rich import print
from infra.db import Anime, db

@click.command()
@click.argument('title')
def open(title: str):
  print('Title: [orange_red1]{}[/orange_red1]'.format(title))

  anime = Anime.get(Anime.title == title)

  print('[bold green]Found![/bold green]')

  print('{}'.format(anime.url))

  db.close()
