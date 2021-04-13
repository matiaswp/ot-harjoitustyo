from database_connection import get_database_connection

def drop_tables(connection):
    cursor = connection.cursor()
    cursor.execute("DROP TABLE IF EXISTS highscores;")

    connection.commit()

def create_table(connection):
    cursor = connection.cursor()
    cursor.execute("create table highscores (id INTEGER primary key, " +
        "name TEXT, score INTEGER);")

    connection.commit()

def initialize():
    connection = get_database_connection()
    drop_tables(connection)
    create_table(connection)


if __name__ == "__main__":
    initialize()