# [Peewee ORM](https://docs.peewee-orm.com/en/latest/peewee/quickstart.html)

## ✨ Important
- We are using **peewee** orm with **sqlite**
- Our models/entities are in `db.py` (should be in `models` dir)

## 📜 Peewee Documentation In a Nutshell
```py
# Importation
import peewee as pw # docs: from peewee import *

# sqlite
db = pw.SqliteDatabase('users.db')

# Defining a model/entity
class User(pw.Model):
  name = pw.CharField()
  email = pw.CharField()
  age = pw.IntegerField()

  class Meta:
    database = db # this model uses the "users.db" database

# Try to connect and see if no error happens
db.connect()

# Create table
db.create_tables([User])

# Storing data (insertion)
user = User(name='user', email='user@example.com', age=30)
user.save()
# or
user = User.create(name='user', email='user@example.com', age=30)

# Retrieving data (query)
# Single query
user = User.select().where(User.name == 'user').get()
# or
user = User.get(User.name == 'user') # shorthand

# List of users
for user in User.select():
  print(user.name)

# Sorting
for user in User.select().order_by(User.age.desc()) # oldest to youngest

# Remember to close the connection
db.close()
```
