import click
from pathlib import Path
from rich import print
from components.icons import Icon
from infra.db import Anime, db

@click.command()
@click.argument('file', required=False)
def save(file: str):
  """Save the whole database into a csv file"""
  resolvedFile = Path(file or 'animes.csv').resolve()

  f = open(resolvedFile, 'a')
  f.write('Title, URL, Created At\n')

  query = Anime.select().order_by(Anime.created_at)

  print('{} Querying...'.format(Icon.INTERROGATIVE.value))
  print('{} Saving in {}'.format(Icon.PLUS.value, file or 'animes.csv'))

  for anime in query:
    f.write('{}, {}, {}\n'.format(anime.title, anime.url, anime.created_at))

  print('[green]Done![/green]')

  f.close()
  db.close()
