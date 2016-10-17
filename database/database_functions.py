import sqlite3
from database.database_settings import DATABASE_NAME

def connect():
    con = sqlite3.connect(DATABASE_NAME)
    return con

def insert_camper_into_db(first_name, last_name, birth_date, gender, address):
    conn = connect()
    cur = conn.cursor()
    sql_query = "insert into Campers(first_name, last_name, date_of_birth, gender, address) values(?,?,?,?,?)"
    cur.execute(sql_query,(first_name, last_name, birth_date, gender, address))
    conn.commit()
    conn.close()

def select_camper_by_id(camper_id):
    conn = connect()
    cur = conn.cursor()
    sql_query = "select first_name, last_name, date_of_birth, gender, address from Campers where camper_id = ?"
    cur.execute(sql_query,(camper_id,))
    data = cur.fetchone()
    conn.close()
    return data

def update_camper_to_db(camper_id, first_name, last_name, birth_date, gender, address):
    conn = connect()
    cur = conn.cursor()
    sql_query = "update Campers set first_name = ?, last_name = ?, date_of_birth = ?, gender = ?, address = ? where camper_id = ?"
    cur.execute(sql_query,(first_name, last_name, birth_date, gender, address, camper_id))
    conn.commit()
    conn.close()

def delete_camper_by_id(camper_id):
    conn = connect()
    cur = conn.cursor()
    sql_query = "delete from Campers where camper_id = ?"
    cur.execute(sql_query,(camper_id,))
    conn.commit()
    conn.close()

def get_all_campers_ids():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("select camper_id from Campers")
    data = cursor.fetchall()
    conn.close()
    return data

def insert_camp_into_db(start_date, end_date, bunck_num, team_num, cost):
    conn = connect()
    cur = conn.cursor()
    sql_query = "insert into Camps(start_date, end_date, bunckhouses_number, teams_number, cost) values(?,?,?,?,?)"
    cur.execute(sql_query,(start_date, end_date, bunck_num, team_num, cost))
    conn.commit()
    conn.close()

def update_camp_to_db(camp_id, start_date, end_date, bunck_num, team_num, cost):
    conn = connect()
    cur = conn.cursor()
    sql_query = "update Camps set start_date = ?, end_date = ?, bunckhouses_number = ?, teams_number = ?, cost = ? where camp_id = ?"
    cur.execute(sql_query,(start_date, end_date, bunck_num, team_num, cost, camp_id))
    conn.commit()
    conn.close()

def select_camp_by_id(camp_id):
    conn = connect()
    cur = conn.cursor()
    sql_query = "select start_date, end_date, bunckhouses_number, teams_number, cost from Camps where camp_id = ?"
    cur.execute(sql_query,(camp_id,))
    data = cur.fetchone()
    conn.close()
    return data

def delete_camp_by_id(camp_id):
    conn = connect()
    cur = conn.cursor()
    sql_query = "delete from Camps where camp_id = ?"
    cur.execute(sql_query,(camp_id,))
    conn.commit()
    conn.close()

def get_all_camps_ids():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("select camp_id from Camps")
    data = cursor.fetchall()
    conn.close()
    return data

def insert_payment_into_db(camper_id, camp_id, payment_date, paid_amount):
    conn = connect()
    cur = conn.cursor()
    sql_query = "insert into Payments (camper_id, camp_id, application_mail_date, paid) values (?,?,?,?)"
    cur.execute(sql_query,(camper_id, camp_id, payment_date, paid_amount))
    conn.commit()
    conn.close()

def update_payment_to_db(payment_id, camper_id, camp_id, payment_date, paid_amount):
    pass

def select_payment_by_id(payment_id):
    conn = connect()
    cur = conn.cursor()
    sql_query = "select camper_id, camp_id, application_mail_date, paid from Payments where payment_id = ?"
    cur.execute(sql_query,(payment_id,))
    data = cur.fetchone()
    conn.close()
    return data

def delete_payment_by_id(payment_id):
    conn = connect()
    cur = conn.cursor()
    sql_query = "delete from Payments where payment_id = ?"
    cur.execute(sql_query,(payment_id,))
    conn.commit()
    conn.close()

def get_all_payments_ids():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("select payment_id from Payments")
    data = cursor.fetchall()
    conn.close()
    return data

def select_username_password(username, password):
    conn = connect()
    cur = conn.cursor()
    sql_query = "select is_admin from Users where username = ? and password = ?"
    cur.execute(sql_query, (username, password))
    data = cur.fetchone()
    conn.close()
    return data

def select_camp_id_by_date(start_date, end_date):
    conn = connect()
    cur = conn.cursor()
    sql_query = "select camp_id from Camps where start_date = ? and end_date = ?"
    cur.execute(sql_query, (start_date, end_date))
    data = cur.fetchone()
    conn.close()
    return data

def insert_bunkhouse_db(campers_gender, camp_id, num_campers):
    print campers_gender, camp_id, num_campers
    conn = connect()
    cur = conn.cursor()
    sql_query = "insert into BunkHouses(campers_gender, camp_id, num_campers) values (?,?,?)"
    cur.execute(sql_query,(campers_gender, camp_id, num_campers))
    conn.commit()
    conn.close()

def insert_team_db(camp_id, team_name, num_campers):
    conn = connect()
    cur = conn.cursor()
    sql_query = "insert into Teams (camp_id, team_name, num_campers) values (?,?,?)"
    cur.execute(sql_query,(camp_id, team_name, num_campers))
    conn.commit()
    conn.close()

def get_camp_num_bunkhouse_team_db(camp_id):
    conn = connect()
    cur = conn.cursor()
    sql_query = "select bunckhouses_number, teams_number from Camps where camp_id = ?"
    cur.execute(sql_query, (camp_id, ))
    data = cur.fetchone()
    conn.close()
    return data

def select_available_bunkhouse(gender, camp_id):
    conn = connect()
    cur = conn.cursor()
    sql_query = "select bunk_house_id from BunkHouses where campers_gender = ? and camp_id = ? and checked_in_num < num_campers"
    cur.execute(sql_query, (gender, camp_id))
    data = cur.fetchall()
    conn.close()
    return data

def select_available_team(camp_id):
    conn = connect()
    cur = conn.cursor()
    sql_query = "select team_id from Teams where camp_id = ? and checked_in_num < num_campers"
    cur.execute(sql_query, (camp_id,))
    data = cur.fetchall()
    conn.close()
    return data

def increment_checked_in_num_bunkhouse(bunkhouse_id):
    conn = connect()
    cur = conn.cursor()
    sql_query = "update BunkHouses set checked_in_num = checked_in_num + 1 where bunk_house_id = ?"
    cur.execute(sql_query,(bunkhouse_id,))
    conn.commit()
    conn.close()

def increment_checked_in_num_team(team_id):
    conn = connect()
    cur = conn.cursor()
    sql_query = "update Teams set  checked_in_num = checked_in_num + 1 where team_id = ?"
    cur.execute(sql_query,(team_id,))
    conn.commit()
    conn.close()

def insert_check_in_record(camper_id,camp_id,team_id,bunk_house_id):
    conn = connect()
    cur = conn.cursor()
    sql_query = "insert into Camper_Camp_BunckHouse_Team(camper_id,camp_id,team_id,bunk_house_id,student_checked_in) values (?,?,?,?,'yes')"
    cur.execute(sql_query,(camper_id,camp_id,team_id,bunk_house_id))
    conn.commit()
    conn.close()

def select_camp_team_bunkhouse_db(camper_id):
    conn = connect()
    cur = conn.cursor()
    sql_query = "select camp_id, team_id, bunk_house_id from Camper_Camp_BunckHouse_Team where camper_id = ?"
    cur.execute(sql_query, (camper_id,))
    data = cur.fetchall()
    conn.close()
    return data

def update_bunkhouses_num_db(num):
    conn = connect()
    cur = conn.cursor()
    sql_query = "update BunkHouses set num_campers = ?"
    cur.execute(sql_query,(num,))
    conn.commit()
    conn.close()

def update_teams_num_db(num):
    conn = connect()
    cur = conn.cursor()
    sql_query = "update Teams set num_campers = ?"
    cur.execute(sql_query,(num,))
    conn.commit()
    conn.close()

def get_all_teams_id_db():
    conn = connect()
    cur = conn.cursor()
    sql_query = "select team_id from Teams"
    cur.execute(sql_query)
    data = cur.fetchall()
    conn.close()
    return data

def select_team_by_id(team_id):
    conn = connect()
    cur = conn.cursor()
    sql_query = "select camp_id, team_name, num_campers, checked_in_num from Teams where team_id = ?"
    cur.execute(sql_query, (team_id,))
    data = cur.fetchone()
    conn.close()
    return data

def get_all_bunkhouses_id_db():
    conn = connect()
    cur = conn.cursor()
    sql_query = "select bunk_house_id from BunkHouses"
    cur.execute(sql_query)
    data = cur.fetchall()
    conn.close()
    return data

def select_bunkhouse_by_id(bunkhouse_id):
    conn = connect()
    cur = conn.cursor()
    sql_query = "select campers_gender, camp_id, num_campers, checked_in_num from BunkHouses where bunk_house_id = ?"
    cur.execute(sql_query, (bunkhouse_id,))
    data = cur.fetchone()
    conn.close()
    return data

def decrement_checked_in_num_bunkhouse(bunkhouse_id):
    conn = connect()
    cur = conn.cursor()
    sql_query = "update BunkHouses set checked_in_num = checked_in_num - 1 where bunk_house_id = ?"
    cur.execute(sql_query,(bunkhouse_id,))
    conn.commit()
    conn.close()

def decrement_checked_in_num_team(team_id):
    conn = connect()
    cur = conn.cursor()
    sql_query = "update Teams set  checked_in_num = checked_in_num - 1 where team_id = ?"
    cur.execute(sql_query,(team_id,))
    conn.commit()
    conn.close()

def update_team_id_checked_in(camper_id, camp_id, team_id):
    conn = connect()
    cur = conn.cursor()
    sql_query = "update Camper_Camp_BunckHouse_Team set  team_id = ? where camper_id = ? and camp_id = ?"
    cur.execute(sql_query,(team_id, camper_id, camp_id))
    conn.commit()
    conn.close()

def update_bunkhouse_id_checked_in(camper_id, camp_id, bunkhouse_id):
    conn = connect()
    cur = conn.cursor()
    sql_query = "update Camper_Camp_BunckHouse_Team set  bunk_house_id = ? where camper_id = ? and camp_id = ?"
    cur.execute(sql_query,(bunkhouse_id, camper_id, camp_id))
    conn.commit()
    conn.close()

def get_all_query_data_db():
    conn = connect()
    cur = conn.cursor()
    sql_query = """
    select Camper_Camp_BunckHouse_Team.bunk_house_id,
    Camper_Camp_BunckHouse_Team.camp_id,
    Camps.start_date, Camps.end_date, Camper_Camp_BunckHouse_Team.camper_id,
    Campers.first_name, Campers.last_name, Campers.gender, Camper_Camp_BunckHouse_Team.team_id
    from Camper_Camp_BunckHouse_Team, Campers , Camps
    where Camper_Camp_BunckHouse_Team.camper_id = Campers.camper_id and Camper_Camp_BunckHouse_Team.camp_id = Camps.camp_id
    """
    cur.execute(sql_query)
    data = cur.fetchall()
    conn.close()
    return data

def update_bunkhouse_id_checked_in(camper_id, camp_id):
    conn = connect()
    cur = conn.cursor()
    sql_query = "update Camper_Camp_BunckHouse_Team set  student_checked_in = 'Yes' where camper_id = ? and camp_id = ?"
    cur.execute(sql_query,(camper_id, camp_id))
    conn.commit()
    conn.close()

