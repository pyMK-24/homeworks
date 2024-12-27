import sqlite3

def create_connection(db_file):
    connection = None
    try:
        connection = sqlite3.connect(db_file)
    except sqlite3.Error as e:
        print(e)
    return connection

def extract_cities(connection):
    sql_extract_cities = '''SELECT id, title FROM cities'''
    cursor = connection.cursor()
    cursor.execute(sql_extract_cities, )
    return cursor.fetchall()

def extract_students_by_city(connection, city_id):
    sql_extract_students = '''SELECT s.first_name, s.last_name, c.title AS city, co.title AS country, c.area
                              FROM students s
                              JOIN cities c ON s.city_id = c.id
                              JOIN countries co ON c.country_id = co.id
                              WHERE c.id = ?'''
    cursor = connection.cursor()
    cursor.execute(sql_extract_students, (city_id,))
    return cursor.fetchall()

def start():
    db_file = 'countries.db'
    conn = create_connection(db_file)
    if conn is None:
        print("Не удалось подключиться к базе данных.")
        return

    while True:
        print("Вы можете отобразить список учеников по выбранному id города из перечня городов ниже, для выхода из программы введите 0:")

        cities = extract_cities(conn)
        for city in cities:
            print(f"ID: {city[0]} - Город: {city[1]}")

        city_id = int(input("Введите ID города (или 0 для выхода): "))

        if city_id == 0:
            print("Выход из программы.")
            break

        city_found = False
        for city in cities:
            if city[0] == city_id:
                city_found = True
                break

        if city_found:
            students = extract_students_by_city(conn, city_id)
            if students:
                print("Список учеников:")
                for student in students:
                    print(f"Имя: {student[0]}, Фамилия: {student[1]}, Страна: {student[3]}, Город: {student[2]}, Площадь города: {student[4]}")
            else:
                print("Нет учеников в этом городе.")
        else:
            print("Некорректный ID города. Попробуйте снова.")

    conn.close()

if __name__ == "__main__":
    start()
