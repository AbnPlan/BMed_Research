import sqlite3
from sqlite3 import Error
from sqlite3.dbapi2 import SQLITE_INSERT

def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

def execute_query(db_name, query):
    cursor = db_name.cursor()
    try:
        cursor.execute(query)
        db_name.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

def insert_data(db_name, name, phone, address1, address2, town, country, zip_code):
    insert_data = f'''
    INSERT INTO patient
    VALUES ('{name}','{phone}','{address1}','{address2}','{town}','{country}','{zip_code}');
    '''
    execute_query(db_name, insert_data)

def db_connection():
    connection = create_connection("DATABASE\\patient_info.db")
    create_users_table = """
	CREATE TABLE IF NOT EXISTS patient (
	name TEXT NOT NULL,
	phone TEXT NOT NULL,
	adress1 TEXT NOT NULL,
	adress2 TEXT,
    town TEXT NOT NULL,
    country TEXT NOT NULL,
    zip_code TEXT NOT NULL
    );
    """
    execute_query(connection, create_users_table)

    return connection
