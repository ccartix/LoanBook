import time


class View:
    def show_menu(self):
        while True:
            print("Меню:")
            print("1. Вивід назв таблиць")
            print("2. Вивід імен стовпчиків таблиці")
            print("3. Додавання даних в таблицю")
            print("4. Оновлення даних в таблиці")
            print("5. Видалення даних в таблиці")
            print("6. Генерування даних в таблицю")
            print("7. Вихід")

            choice = input("Зробіть вибір: ")

            if choice in ('1', '2', '3', '4', '5', '6', '7'):
                return choice
            else:
                print("Будь ласка, введіть правильний номер опції (від 1 до 7)")
                time.sleep(2)

    def show_message(self, message):
        print(message)
        time.sleep(2)

    def ask_continue(self):
        agree = input("Продовжити внесення змін? (y/n) ")
        return agree

    def show_tables(self, tables):
        print("Назви таблиць:")
        for table in tables:
            print(table)
        time.sleep(2)

    def ask_table(self):
        table_name = input("Введіть назву таблиці: ")
        return table_name

    def show_columns(self, columns):
        print("Назви стовпців:")
        for column in columns:
            print(column)
        time.sleep(2)

    def insert(self):
        while True:
            try:
                table = input("Введіть назву таблиці: ")
                columns = input("Введіть назви колонок (через пробіл): ").split()
                val = input("Введіть відповідні значення (через пробіл): ").split()

                if len(columns) != len(val):
                    raise ValueError("Кількість стовпців повинна бути дорівнювати кількості значень.")

                return table, columns, val
            except ValueError as e:
                print(f"Помилка: {e}")

    def update(self):
        while True:
            try:
                table = input("Введіть назву таблиці: ")
                column = input("Введіть назву колонки, яку хочете змінити: ")
                id = int(input("Введіть ID рядка, який потрібно змінити: "))
                new_value = input("Введіть нове значення: ")
                return table, column, id, new_value
            except ValueError as e:
                print(f"Помилка: {e}")

    def delete(self):
        while True:
            try:
                table = input("Введіть назву таблиці: ")
                id = int(input("Введіть ID рядка, який потрібно видалити: "))
                return table, id
            except ValueError as e:
                print(f"Помилка: {e}")

    def generate_data_input(self):
        while True:
            try:
                table_name = input("Введіть назву таблиці: ")
                num_rows = int(input("Введіть кількість рядків для генерації: "))
                return table_name, num_rows
            except ValueError as e:
                print(f"Помилка: {e}")
