import sqlite3

db_path = 'N:\projects\WhoseAround\db'

def connect_to_database(db_path):
    conn = sqlite3.connect(db_path)
    return conn

def add_game(conn, game_name):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Games (game_name) VALUES (?)", (game_name,))
    conn.commit()

def add_user(conn, discord_id, username):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Users (discord_id, username) VALUES (?, ?)", (discord_id, username))
    conn.commit()

def add_interest(conn, user_id, game_id):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Interests (user_id, game_id) VALUES (?, ?)", (user_id, game_id))
    conn.commit()

def add_schedule(conn, user_id, game_id, scheduled_time):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Schedules (user_id, game_id, scheduled_time) VALUES (?, ?, ?)", (user_id, game_id, scheduled_time))
    conn.commit()