import sqlite3
from sqlite3 import Error
from sqlite3.dbapi2 import SQLITE_INSERT

def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

def execute_query(db_name, query):
    cursor = db_name.cursor()
    try:
        cursor.execute(query)
        db_name.commit()
    except Error as e:
        print(f"The error '{e}' occurred")


def insert_data(db_name, name, phone, address1, address2, town, country, zip_code, health_insurance):
    insert_data = f'''
    INSERT INTO patient
    VALUES ('{name}','{phone}','{address1}','{address2}','{town}','{country}','{zip_code}', '{health_insurance}');
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
    zip_code TEXT NOT NULL,
    health_insurance TEXT NOT NULL
    );
    """
    execute_query(connection, create_users_table)

    return connection
