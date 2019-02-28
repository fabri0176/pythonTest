from peewee import *
from datetime import date
import uuid


db = SqliteDatabase('people.db')

class Person(Model):
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

def create_family_members():
    UncleTommy = Person(name="Tommy",birthday=date(1991,3,10),is_relative=True)
    UncleTommy.save()

create_family_members()