# function.py
from note import Note
from file_operation import read_file, write_file
from datetime import datetime


def show_all_notes():
    notes = read_file()
    if not notes:
        print("Нет заметок.")
    else:
        for note in notes:
            print(note)


def add_note() -> object:
    title = input("Введите заголовок заметки: ")
    body = input("Введите текст заметки: ")
    new_note = Note(title=title, body=body)
    notes = read_file()
    notes.append(new_note)
    write_file(notes)
    print("Заметка успешно добавлена.")


def delete_note(note_id):
    notes = read_file()
    notes = [note for note in notes if note.id != note_id]
    write_file(notes)
    print("Заметка удалена.")


def edit_note(note_id, new_title, new_body):
    notes = read_file()
    for note in notes:
        if note.id == note_id:
            note.title = new_title
            note.body = new_body
            note.date = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    write_file(notes)
    print("Заметка отредактирована.")


def show_notes_by_date(date):
    notes = read_file()
    matching_notes = [note for note in notes if date in note.date]
    if not matching_notes:
        print(f"Нет заметок на дату {date}.")
    else:
        for note in matching_notes:
            print(note)
