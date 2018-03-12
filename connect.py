import sqlite3

conn = sqlite3.connect('rent.db')
cur = conn.cursor()

def create_table():
    cur.execute('CREATE TABLE IF NOT EXISTS stuffToPlot(County TEXT, State TEXT, Median_Cost REAL)')


def data_entry():
    cur.execute('INSERT INTO stuffToPlot VALUES("Jefferson", "KY", 1000)')
    conn.commit()
    cur.close()
    conn.close()


create_table()
data_entry()
