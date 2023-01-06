from datetime import datetime
import click
from rich import print
from rich.table import Table
from components.icons import Icon
from infra.db import Anime, db

@click.command()
def list():
  """Query and show all the saved animes"""
  table = Table(title="Anime List")

  table.add_column("Title", style="magenta")
  table.add_column("Created at", justify="right", style="cyan", no_wrap=True)

  print('{} Querying today animes...'.format(Icon.PLUS.value))

  query = Anime.select(
    Anime.title,
    Anime.created_at
  ).where(Anime.created_at.day == datetime.now().day).order_by(Anime.created_at.desc())

  for anime in query:
    created_at, ms = anime.created_at.split('.')
    table.add_row(anime.title, created_at)

  print('[green]Done![/green]')
  print(table)

  db.close()
