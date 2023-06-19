import sqlite3


class User:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender


def create_user_table(cursor):
    command = """
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY,
        name TEXT,
        surname TEXT,
        gender TEXT
    );
    """
    cursor.execute(command)


def add_user(cursor, user):
    command = """
    INSERT INTO users(name, surname, gender) VALUES (?, ?, ?);
    """
    cursor.execute(command, (user.name, user.surname, user.gender))


def get_users_list(cursor):
    command = """
    SELECT * FROM users;
    """
    result = cursor.execute(command)
    users = result.fetchall()
    print(*users, sep='\n')


def get_user_by_id(cursor, id_user):
    command = """
    SELECT * FROM users
    WHERE id = ?;
    """
    result = cursor.execute(command, (id_user, ))
    user = result.fetchall()
    if len(user) == 0:
        print('Пользователя не существует')
    else:
        print(*user)


def get_users_by_gender(cursor, gender):
    command = """
    SELECT * FROM USERS
    WHERE gender = ?;
    """
    result = cursor.execute(command, (gender, ))
    users = result.fetchall()
    print(*users, sep='\n')


def delete_user_by_id(cursor, id_user):
    command = """
    DELETE FROM USERS
    WHERE id = ?;
    """
    cursor.execute(command, (id_user, ))


def update_user_name(cursor, new_name, user_id):
    command = """
    UPDATE users SET name = ? WHERE id = ?;
    """
    cursor.execute(command, (new_name, user_id))


def delete_users(cursor):
    command = """
    DELETE FROM users;
    """
    cursor.execute(command)


if __name__ == '__main__':
    with sqlite3.connect('data.db') as curs:
        create_user_table(curs)
        # add_user(curs, User('Наталья', 'Черновол', 'Женский'))
        # add_user(curs, User('Юрий', 'Кузнецов', 'Мужской'))
        # add_user(curs, User('Елизавета', 'Иванова', 'Женский'))
        # update_user_name(curs, 'Мария', 3)
        get_users_by_gender(curs, 'Женский')
