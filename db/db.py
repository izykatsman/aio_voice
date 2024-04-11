from mysql.connector import connect, Error

import config


def get_hellow():
    connection = connect(host=config.bd_host, user=config.bd_login, password=config.bd_pass, database=config.bd_base)
    q = connection.cursor(dictionary=True)
    q.execute(f'''SELECT `text`, `image` FROM `hellow`''')
    return q.fetchone()


def get_all_chats():
    connection = connect(host=config.bd_host, user=config.bd_login, password=config.bd_pass, database=config.bd_base)
    q = connection.cursor(dictionary=True)
    q.execute(f'''SELECT `id` FROM `chat`''')
    return q.fetchall()


def set_new_chat(chat_id: int, username: str):
    connection = connect(host=config.bd_host, user=config.bd_login, password=config.bd_pass, database=config.bd_base)
    q = connection.cursor()
    q.execute("INSERT INTO `chat` (id, username) VALUES ('%s','%s')" % (chat_id, username))
    connection.commit()


def get_chat(chat_id):
    connection = connect(host=config.bd_host, user=config.bd_login, password=config.bd_pass, database=config.bd_base)
    q = connection.cursor(dictionary=True)
    q.execute(f'''SELECT `id` FROM `chat` where id = {chat_id}''')
    return q.fetchone()


def set_new_user(chat_id: int, username: str):
    connection = connect(host=config.bd_host, user=config.bd_login, password=config.bd_pass, database=config.bd_base)
    q = connection.cursor()
    q.execute("INSERT INTO `user` (id, username) VALUES ('%s','%s')" % (chat_id, username))
    connection.commit()


def get_user(user_id):
    connection = connect(host=config.bd_host, user=config.bd_login, password=config.bd_pass, database=config.bd_base)
    q = connection.cursor(dictionary=True)
    q.execute(f'''SELECT `id` FROM `user` where id = {user_id}''')
    return q.fetchone()

