import click
from datetime import datetime
from rich import print
from rich.table import Table

from components.icons import Icon
from infra.db import Anime, db


@click.command()
@click.option('--all', '-a', is_flag=True, help='List all available animes')
def list(all: bool):
  """Query and show today animes"""
  table = Table(title="Anime List")

  table.add_column("Title", style="magenta")
  table.add_column("Created at", justify="right", style="cyan", no_wrap=True)

  print(f'{Icon.INTERROGATIVE.value} Querying animes...')

  totalCount = Anime.select().count()
  print(f'{Icon.PLUS.value} Animes count: {totalCount}')

  query = Anime.select(
    Anime.title,
    Anime.created_at
  ).where(
    Anime.created_at.day == datetime.now().day
  ).order_by(Anime.created_at.desc())

  if all:
    query = Anime.select(
      Anime.title,
      Anime.created_at
    ).order_by(Anime.created_at.desc())

  for anime in query:
    created_at, ms = anime.created_at.split('.')
    table.add_row(anime.title, created_at)

  if table.row_count == 0:
    print(f'{Icon.MINUS.value} [bold red]No anime saved today. Try again with -a!')
    exit(0)

  print('[bold green]Done!')
  print(table)

  db.close()
