import sqlite3

try:
    # Создание соединения с базой данных
    conn = sqlite3.connect('students.db')

    # Создание курсора для выполнения операций с базой данных
    cursor = conn.cursor()

    # Создание таблицы студентов
    cursor.execute('''CREATE TABLE IF NOT EXISTS students (
                      id INTEGER PRIMARY KEY,
                      surname TEXT,
                      name TEXT,
                      birth_year INTEGER,
                      birth_month INTEGER,
                      birth_day INTEGER)''')

    # Создание таблицы зачеток
    cursor.execute('''CREATE TABLE IF NOT EXISTS records (
                      id INTEGER PRIMARY KEY,
                      student_id INTEGER,
                      subject TEXT,
                      exam_date TEXT,
                      teacher TEXT,
                      FOREIGN KEY (student_id) REFERENCES students(id))''')

    # Заполнение таблицы студентов
    students_data = [
        ('Иванов', 'Иван', 2000, 5, 15),
        ('Петров', 'Петр', 1999, 9, 23),
        ('Сидоров', 'Алексей', 2001, 12, 7),
        ('Козлов', 'Дмитрий', 1998, 3, 11),
        ('Смирнова', 'Анна', 2002, 7, 3)
    ]
    cursor.executemany('INSERT INTO students (surname, name, birth_year, birth_month, birth_day) VALUES (?, ?, ?, ?, ?)', students_data)

    # Заполнение таблицы зачеток
    records_data = [
        (1, 'Математический анализ', '2024-06-10', 'Иванов Иван Иванович'),
        (2, 'Философия', '2024-06-12', 'Петров Петр Петрович'),
        (3, 'Физика', '2024-06-14', 'Сидоров Алексей Владимирович'),
        (4, 'История', '2024-06-16', 'Козлов Дмитрий Сергеевич'),
        (5, 'Языки программирования', '2024-06-18', 'Смирнова Анна Александровна')
    ]
    cursor.executemany('INSERT INTO records (student_id, subject, exam_date, teacher) VALUES (?, ?, ?, ?)', records_data)

    # Сохранение изменений
    conn.commit()

    print("База данных успешно создана и заполнена!")

except sqlite3.Error as e:
    print("Ошибка SQLite:", e)

finally:
    # Закрытие соединения
    if conn:
        conn.close()

def print_table(rows, header):
    print("|".join(header))
    print("-" * (len(header)*20))
    for row in rows:
        print("|".join(str(cell) for cell in row))

# Создание соединения с базой данных
conn = sqlite3.connect('students.db')

# Создание курсора для выполнения операций с базой данных
cursor = conn.cursor()

# Запрос на выборку всех дат экзаменов
cursor.execute("SELECT exam_date FROM records")

# Получение результатов запроса
exam_dates = cursor.fetchall()

# Вывод результатов в виде таблицы
print_table(exam_dates, ["Дата экзамена"])

# Закрытие соединения
conn.close()
