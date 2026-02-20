import sqlite3

DB_NAME = 'MoviesInfo64'

def init_db():
    conn = sqlite3.connect(DB_NAME)
    conn.commit()
    conn.close()
# init_db()
def create_table():
    query = '''
            CREATE TABLE IF NOT EXISTS Movie
            (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            year TEXT,
            country TEXT,
            imdb_rate TEXT,
            genres TEXT
            )
            '''
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
    conn.close()
# create_table()
def save_movie(movie: dict):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    query = ''' INSERT INTO Movie (title, year, country, imdb_rate, genres)
    VALUSE (?, ?, ?, ?, ?)'''
    cursor.execute(query, 
    (movie["title"],
    movie["year"],
    movie["country"],
    movie["imdb_rate"],
    movie["genres"],
    ))

def get_all_movies():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Movie")
    rows = cursor.fetchall()
    conn.close()
    return rows

                                          
                            
