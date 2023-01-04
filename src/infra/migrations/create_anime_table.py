from infra.db import db, Anime

def create_anime_table():
  db.create_tables([Anime])

if __name__ == '__main__':
  create_anime_table()
