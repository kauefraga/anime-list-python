import click
from infra.db import Anime, db

@click.command()
def list():
  for anime in Anime.select().order_by(Anime.created_at.desc()):
    print(anime.title, anime.created_at)

  db.close()
