# note.py
import uuid
from datetime import datetime


class Note:
    def __init__(self, id=str(uuid.uuid1())[:8], title="Заголовок", body="Текст заметки", date=None):
        self.id = id
        self.title = title
        self.body = body
        self.date = date or datetime.now().strftime("%d.%m.%Y %H:%M:%S")

    def to_dict(self):
        return {'id': self.id, 'title': self.title, 'body': self.body, 'date': self.date}

    @classmethod
    def from_dict(cls, data):
        return cls(id=data['id'], title=data['title'], body=data['body'], date=data['date'])

    def __str__(self):
        return f"ID: {self.id}\nЗаголовок: {self.title}\nТекст: {self.body}\nДата: {self.date}"
