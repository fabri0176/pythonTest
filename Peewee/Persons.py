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
    owner = ForeignKeyField(Person, related_name='pets')
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

    Madre = Person(name = "Luz Marina",birthday=date(1968,5,19),is_relative = True)
    Madre.save()

    tommys_dog = Pet.create(owner = UncleTommy, name ="Fido", animal_type = "Gato")
    anas_cat = Pet.create(owner=Madre,name="Asly",animal_type="Gato")

    tommys_dog.name = 'Firulais'
    tommys_dog.save()

def get_family_pets():
    for person in Person.select():
        if(person.id is not None):
            person.name += "Concatena"
            person.save()

# get_family_pets()
# create_family_members()

def get_family_member():

    try:
        grandma = Person.select().where(Person.id == 6).get()
        print(grandma)
        print("Existe el registro {}".format(grandma.name))
    except:
        print("No existe el registro")

    try:
        persona = Person.select().where(Person.name == 'TommyConcatena').get()
        print("Existe el registro {}".format(persona.name))
    except:
        print("No existe el registro 2")

get_family_member()


def delete_pet(name):
    query = Pet.delete().where(Pet.name==name)
    deleted_entries = query.execute()
    print("{} Registros Borrados".format(deleted_entries))

delete_pet("Asly")