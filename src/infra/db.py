import peewee as pw

db = pw.SqliteDatabase('animes.db')

class Anime(pw.Model):
  title = pw.CharField(unique=True)
  # alias = pw.CharField()
  url = pw.CharField()
  created_at = pw.DateTimeField(formats='YYYY-MM-DD HH:MM:SS')

  class Meta:
    database = db
