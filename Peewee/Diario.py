from peewee import *
import datetime
import uuid
import  sys
from collections import  OrderedDict

db = SqliteDatabase('diary.db')



class Entry(Model):
    # Content

    # timestamp
    content = TextField()
    timestamp = DateTimeField(default=datetime.datetime.now())
    class Meta:
        database = db

def menu_loop():
    """Show menu"""
    choice = None

    while choice != 'q':
        print("Press 'q' to quit")
        for key,value in menu.items():
            print("{}) {}".format(key,value.__doc__))
        choice = input("Action: ").lower().strip()

        if choice in menu:
            menu[choice]()



def add_entry():
    """Add Entry"""
    print("Enter your thoughts. Press Ctrl +D to finish")
    data = input().strip()

    if data:
        if input("Desea guardar s/n").lower().strip() != 'n':
            Entry.create(content = data )
            print("Registro guardado correctamente")

def view_entries():
    """View all entries"""
    entries = Entry.select().order_by(Entry.timestamp.desc())

    for entry in entries:
        timestamp = entry.timestamp.strftime("%A %B %Y %I:%M%p")
        print(timestamp)
        print("*"*len(timestamp))
        print(entry.content)
        print("*" * len(timestamp))
        print('n) next entry')
        print('q) regresar al menu')

        next_action = input("Action:")

        if next_action == 'q':
            break
def delete_entry(entry):
    """Delete an Entry"""

menu = OrderedDict([
    ('a',add_entry),
    ('v',view_entries),
    ('d',delete_entry)
])


def create_and_connect():
    db.connect()
    db.create_tables([Entry], safe=True)

create_and_connect()
if __name__ == '__main__':
    print("Se ejecuta solo cuando es llamado el archivo directamente")
    menu_loop()


