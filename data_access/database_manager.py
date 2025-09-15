from view.user_view import *
from view.user_view import *
def create_table_user():
    connection = sqlite3.connect("mft_db.db")
    cursor = connection.cursor()
    cursor.execute("insert into users (user_name,password,nick_name,locked) values = (?,?,?,?,)"
                   [user_name.get(), password.get(), nick_name.get(), locked.get()])
    connection.commit()
    connection.close()


def save_user(user_name, password, nickname, locked):
     connection = sqlite3.connect("mft_db.db")
     cursor = connection.cursor()
     cursor.execute("creat table users (id integer, user_name text, password text, nickname text,locked boolean)")

     connection.commit()
     connection.close()






