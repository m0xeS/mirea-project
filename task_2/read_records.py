import sqlite3

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