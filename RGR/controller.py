import sys

from model import Model
from view import View


class Controller:
    def __init__(self):
        self.view = View()
        try:
            self.model = Model()
            self.view.show_message("Підключено до бази даних")
        except Exception as e:
            self.view.show_message(f"Сталася помилка під час ініціалізації: {e}")
            sys.exit(1)

    def run(self):
        while True:
            choice = self.view.show_menu()
            if choice == '1':
                self.view_tables()
            elif choice == '2':
                self.view_columns()
            elif choice == '3':
                self.add_data()
            elif choice == '4':
                self.update_data()
            elif choice == '5':
                self.delete_data()
            elif choice == '6':
                self.generate_data()
            elif choice == '7':
                break

    def view_tables(self):
        tables = self.model.get_all_tables()
        self.view.show_tables(tables)

    def view_columns(self):
        table_name = self.view.ask_table()
        columns = self.model.get_all_columns(table_name)
        self.view.show_columns(columns)

    def add_data(self):
        while True:
            table, columns, val = self.view.insert()
            error = self.model.add_data(table, columns, val)
            if int(error) == 1:
                self.view.show_message("Дані додано успішно!")
                agree = self.view.ask_continue()
                if agree == 'n':
                    break
            elif int(error) == 2:
                self.view.show_message("Унікальний ідентифікатор вже існує!")
                agree = self.view.ask_continue()
                if agree == 'n':
                    break
            else:
                self.view.show_message("Недійсний зовнішній ключ")
                agree = self.view.ask_continue()
                if agree == 'n':
                    break

    def update_data(self):
        while True:
            table, column, id, new_value = self.view.update()
            error = self.model.update_data(table, column, id, new_value)
            if int(error) == 1:
                self.view.show_message("Дані оновлено успішно!")
                agree = self.view.ask_continue()
                if agree == 'n':
                    break
            elif int(error) == 2:
                self.view.show_message(f"Унікальний ідентифікатор {new_value} вже існує!")
                agree = self.view.ask_continue()
                if agree == 'n':
                    break
            else:
                self.view.show_message(f"Недійсний зовнішній ключ {new_value} у колонці {column}")
                agree = self.view.ask_continue()
                if agree == 'n':
                    break

    def delete_data(self):
        while True:
            table, id = self.view.delete()
            error = self.model.delete_data(table, id)
            if int(error) == 1:
                self.view.show_message("Рядок видалено успішно!")
                agree = self.view.ask_continue()
                if agree == 'n':
                    break
            else:
                self.view.show_message("Неможливо видалити рядок, оскільки існують зв\'язані дані")
                agree = self.view.ask_continue()
                if agree == 'n':
                    break

    def generate_data(self):
        table_name, num_rows = self.view.generate_data_input()
        self.model.generate_data(table_name, num_rows)
        self.view.show_message(f"Дані для таблиці {table_name} були згенеровані успішно")
