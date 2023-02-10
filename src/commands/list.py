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

  print('{} Querying animes...'.format(Icon.INTERROGATIVE.value))

  totalCount = Anime.select().count()
  print('{} Animes count: {}'.format(Icon.PLUS.value, totalCount))

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
    print('{} [bold red]No anime saved today. Try again with -a![/bold red]'.format(Icon.MINUS.value))
    exit(0)

  print('[bold green]Done![/bold green]')
  print(table)

  db.close()
