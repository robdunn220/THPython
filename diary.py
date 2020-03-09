from peewee import *
import datetime


db = SqliteDatabase('diary.db')


class Entry(Model):
    content = TextField()
    timestamp = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db


def initialize():
    db.connect()
    db.create_tables([Entry], safe=True)


def menu_loop():
    """Show menu"""


def add_entry():
    """Add entry"""


def view_entries():
    """View entries"""


def delete_entry():
    """Delete entry"""


if __name__ == '__main__':
    initialize()
    menu_loop()
