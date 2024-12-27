import sqlite3

def create_connection(db_file):
    connection = None
    try:
        connection = sqlite3.connect(db_file)
    except sqlite3.Error as e:
        print(e)
    return connection

def create_table(connection, create_table_sql):
    try:
        cursor = connection.cursor()
        cursor.execute(create_table_sql)
        connection.commit()
    except sqlite3.Error as e:
        print(e)

def insert_countries(connection, countries):
    sql = '''INSERT INTO countries(title)
    VALUES (?)'''
    try:
        cursor = connection.cursor()
        cursor.execute(sql, countries)
        connection.commit()
    except sqlite3.Error as e:
        print(e)

def insert_cities(connection, city_data):
    sql = '''INSERT INTO cities(title, area, country_id)
    VALUES (?, ?, ?)'''
    try:
        cursor = connection.cursor()
        cursor.execute(sql, city_data)
        connection.commit()
    except sqlite3.Error as e:
        print(e)

def insert_students(connection, students):
    sql = '''INSERT INTO students(first_name,last_name,city_id)
    VALUES (?, ?, ?)'''
    try:
        cursor = connection.cursor()
        cursor.execute(sql, students)
        connection.commit()
    except sqlite3.Error as e:
        print(e)

def delete_students(connection,student_id):
    sql = '''DELETE FROM students WHERE id = ?'''
    try:
        cursor = connection.cursor()
        cursor.execute(sql, (student_id,))
        connection.commit()
    except sqlite3.Error as e:
        print(e)

sql_create_table_countries = '''
CREATE TABLE IF NOT EXISTS countries (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL
)'''

sql_create_table_cities = '''
CREATE TABLE IF NOT EXISTS cities (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    area REAL DEFAULT 0,
    country_id INTEGER,
    FOREIGN KEY (country_id) REFERENCES countries(id)
)'''

sql_create_table_students = '''
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    city_id INTEGER,
    FOREIGN KEY (city_id) REFERENCES cities(id)
)'''

my_conn = create_connection('countries.db')
if my_conn is not None:
    print('Successfully connected to the database')
    create_table(my_conn, sql_create_table_countries)
    create_table(my_conn, sql_create_table_cities)
    create_table(my_conn, sql_create_table_students)

# insert_countries(my_conn, ("Russia",))
# insert_countries(my_conn, ("Turkey",))
# insert_countries(my_conn, ("Norway",))
#
# insert_cities(my_conn, ("Moscow", 2561.5, 1))
# insert_cities(my_conn, ("Istanbul", 5461.0, 2))
# insert_cities(my_conn, ("Oslo", 454.0, 3))
# insert_cities(my_conn, ("Beijing", 16410.5, 4))
# insert_cities(my_conn, ("Sydney", 12368.0, 5))
# insert_cities(my_conn, ("Toronto", 630.2, 6))
# insert_cities(my_conn, ("Berlin", 891.8, 7))
#
# insert_students(my_conn, ("Putin", "Vladimir", 1))
# insert_students(my_conn, ("John", "Vatson", 2))
# insert_students(my_conn, ("Olga", "Petrova", 3))
# insert_students(my_conn, ("Li", "Wang", 4))
# insert_students(my_conn, ("Alice", "Johnson", 5))
# insert_students(my_conn, ("David", "Beckham", 6))
# insert_students(my_conn, ("Sophia", "Müller", 7))
# insert_students(my_conn, ("Max", "Verstappen", 1))
# insert_students(my_conn, ("Emma", "Brown", 2))
# insert_students(my_conn, ("Lucas", "George", 3))
# insert_students(my_conn, ("Zhang", "Chong", 4))
# insert_students(my_conn, ("Charlotte", "Davis", 5))
# insert_students(my_conn, ("James", "Bond", 6))
# insert_students(my_conn, ("Liam", "Garcia", 7))
# insert_students(my_conn, ("Benjamin", "Franklin", 2))



my_conn.close()

