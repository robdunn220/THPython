from peewee import *


db = SqliteDatabase('students.db')


class Student(Model):
    username = CharField(max_length=255, unique=True)
    points = IntegerField(default=0)

    class Meta:
        database = db


students = [
    {'username': 'Rob',
     'points': 228},
    {'username': 'Tyler',
     'points': 28},
    {'username': 'Swartz',
     'points': 8}
]


def add_students():
    for student in students:
        try:
            Student.create(username=student['username'],
                           points=student['points'])
        except IntegrityError:
            student_record = Student.get(username=student['username'])
            student_record.points = student['points']
            student_record.save()


def top_student():
    student = Student.select().order_by(Student.points.desc()).get()
    return student


if __name__ == '__main__':
    db.connect()
    db.create_tables([Student], safe=True)
    add_students()
    print('Top Student right now: {0.username} with {0.points} points.'.format(top_student()))
