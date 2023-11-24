# file_operation.py
import json


def write_file(notes):
    with open('notes.json', 'w', encoding='utf-8') as file:
        json.dump([note.to_dict() for note in notes], file, ensure_ascii=False, indent=4)


from note import Note


def read_file():
    array = []
    try:
        with open("notes.json", "r", encoding='utf-8') as file:
            data = json.load(file)
            for item in data:
                note = Note(
                    id=item['id'],
                    title=item['title'],
                    body=item['body'],
                    date=item['date']
                )
                array.append(note)
    except FileNotFoundError:
        print('Файл notes.json не найден...')
    except json.decoder.JSONDecodeError:
        print('Файл notes.json пуст или содержит некорректные данные JSON...')
    return array
