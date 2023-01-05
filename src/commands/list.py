import click
from rich import print
from rich.table import Table
from infra.db import Anime, db

@click.command()
def list():
  """Query and show all the saved animes"""
  table = Table(title="Anime List")

  table.add_column("Title", style="magenta")
  table.add_column("Created at", justify="right", style="cyan", no_wrap=True)

  for anime in Anime.select().order_by(Anime.created_at.desc()):
    created_at, ms = anime.created_at.split('.')
    table.add_row(anime.title, created_at)

  print(table)

  db.close()
