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


def insert_patient(db_name, name, phone, address1, address2, town, country, zip_code, health_insurance):
    insert_data = f'''
    INSERT INTO patient
    VALUES ('{name}','{phone}','{address1}','{address2}','{town}','{country}','{zip_code}', '{health_insurance}');
    '''
    execute_query(db_name, insert_data)


def insert_appointment(db_name, name, emergency, service, 
                    Fiebre,
                    Tos,
                    DiffResp,
                    Escalofrios,
                    Temblores,
                    DolorMuscular,
                    DolorCabeza,
                    DolorGarganta,
                    PerdidaOlfatoGusto):
    insert_data = f'''
    INSERT INTO appointment
    VALUES ('{name}','{emergency}','{service}','{Fiebre}','{Tos}','{DiffResp}','{Escalofrios}','{Temblores}', '{DolorMuscular}', '{DolorCabeza}', '{DolorGarganta}', '{PerdidaOlfatoGusto}');
    '''
    execute_query(db_name, insert_data)

def insert_survey(
    db_name, q1_exp_gen, q2_necessities, 
    q3_info_quality, q4_use_sys, q5_ad_comment, 
    q6_quality, q6_visual, q6_use,
    q6_func, q7_screen, q7_funccionality, q7_info_quality):
    insert_data = f'''
    INSERT INTO survey
    VALUES ('{q1_exp_gen}','{q2_necessities}','{q3_info_quality}','{q4_use_sys}','{q5_ad_comment}','{q6_quality}','{q6_visual}','{q6_use}', '{q6_func}', '{q7_screen}', '{q7_funccionality}', '{q7_info_quality}');
    '''
    execute_query(db_name, insert_data)

def db_connection():
    connection = create_connection("Database.db")
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
    create_apointments_table = """
    CREATE TABLE IF NOT EXISTS appointment (
    name TEXT NOT NULL,
    emergency INT,
    service TEXT NOT NULL,
    fiebre TEXT NOT NULL,
    Tos TEXT NOT NULL,
    diff_resp TEXT NOT NULL,
    escalofrios TEXT NOT NULL,
    temblores TEXT NOT NULL,
    dolor_muscular TEXT NOT NULL,
    dolor_cabeza TEXT NOT NULL,
    dolor_garganta TEXT NOT NULL,
    perdida_olfato_gusto TEXT NOT NULL
    );
    """

    create_survey_table = """
	CREATE TABLE IF NOT EXISTS survey (
    q1_exp_gen INT, 
    q2_necessities INT, 
    q3_info_quality INT, 
    q4_use_sys INT, 
    q5_ad_comment TEXT, 
    q6_quality INT, 
    q6_visual INT, 
    q6_use INT,
    q6_func INT, 
    q7_screen INT, 
    q7_funccionality INT, 
    q7_info_quality INT
    );
    """

    execute_query(connection, create_users_table)
    execute_query(connection, create_apointments_table)
    execute_query(connection, create_survey_table)

    return connection
