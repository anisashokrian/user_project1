import sqlite3


def create_table_user():
    connection = sqlite3.connect("data_access/mft_db.db")
    cursor = connection.cursor()
    cursor.execute(
        "create table if not exists users (id integer primary key autoincrement, user_name text, password text, nickname text,locked boolean)")
    connection.commit()
    connection.close()


def save_user(user_name, password, nickname, locked):
    connection = sqlite3.connect("data_access/mft_db.db")
    cursor = connection.cursor()
    cursor.execute("insert into users (user_name,password,nickname,locked) values (?,?,?,?)",
                   [user_name, password, nickname, locked])
    connection.commit()
    connection.close()


