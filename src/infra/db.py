import peewee as pw

db = pw.SqliteDatabase('animes.db')

class Anime(pw.Model):
  # id = pw.IdentifierField() # primary key
  title = pw.CharField()
  # alias = pw.CharField()
  url = pw.CharField()
  created_at = pw.CharField()

  class Meta:
    database = db # This model uses the "people.db" database.

# entities: Anime, whitelisted sites
