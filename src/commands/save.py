import click
from pathlib import Path
from rich import print

from components.icons import Icon
from infra.db import Anime, db


@click.command()
@click.argument('file', required=False)
def save(file: str):
  """Save the whole database into a csv file"""
  path = Path(file or 'animes.csv').resolve()

  if path.exists():
    f = open(path, 'w')
  else:
    f = open(path, 'a')

  f.write('Title, URL, Created At\n')

  query = Anime.select().order_by(Anime.created_at)

  print(f'{Icon.INTERROGATIVE.value} Querying...')
  print('{} Saving in {}'.format(Icon.PLUS.value, file or 'animes.csv'))

  for anime in query:
    f.write('{}, {}, {}\n'.format(anime.title, anime.url, anime.created_at))

  print('[green]Done!')

  f.close()
  db.close()
