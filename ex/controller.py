from function import *


def run():
    while True:
        print_menu()
        choice = input("Введите номер функции: ")
        if choice == '1':
            show_all_notes()
        elif choice == '2':
            add_note()
        elif choice == '3':
            show_all_notes()
            note_id = input("Введите ID заметки, которую вы хотите удалить: ")
            delete_note(note_id)
        elif choice == '4':
            show_all_notes()
            note_id = input("Введите ID заметки, которую вы хотите изменить: ")
            title = input("Введите новый заголовок: ")
            body = input("Введите новое тело: ")
            edit_note(note_id, title, body)
        elif choice == '5':
            date = input("Введите дату (dd.mm.yyyy): ")
            show_notes_by_date(date)
        elif choice == '6':
            break
        else:
            print("Неверный выбор. Пожалуйста, попробуйте снова.")


def print_menu():
    print("\nМеню:")
    print("1. Показать все заметки")
    print("2. Добавить новую заметку")
    print("3. Удалить заметку")
    print("4. Изменить заметку")
    print("5. Показать заметки по дате")
    print("6. Выход")
