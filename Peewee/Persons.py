from peewee import *

db = SqliteDatabase('people.db')

class Person(Model):
    id = UUIDField(primary_key=True)
    name = CharField()
    birthday = DateField()
    is_relative = BooleanField()

    class Meta:
        database = db


class Pet(Model):
    omner = ForeignKeyField(Person, related_name='pets')
    name = CharField()
    animal_type = CharField()

    class Meta:
        database = db
    
def create_and_connect():
    db.connect()
    db.create_tables([Person, Pet], safe = True)

create_and_connect()