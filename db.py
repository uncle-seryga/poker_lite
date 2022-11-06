import sqlite3


class DB:
    def __init__(self):
        self.__conn = sqlite3.connect('sql/service.db', check_same_thread=False)
        self.__cursor = self.__conn.cursor()
        self.__cursor.execute("""CREATE TABLE IF NOT EXISTS game_number(number)""")
        # self.__cursor.execute("""INSERT INTO game_number VALUES (?)""", (0,))
        self.__conn.commit()

    def new_room(self):
        this_number = self.__cursor.execute("""SELECT number FROM game_number""").fetchone()
        self.__cursor.execute("""UPDATE game_number SET number=(?)""", ((int(this_number[0]) + 1),))
        self.__conn.commit()
        return this_number[0]



