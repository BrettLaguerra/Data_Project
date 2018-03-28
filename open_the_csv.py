import csv
import numpy
import sqlite3

def open_csv(filename, cursor, d=','):
    with open(filename, encoding='latin-1') as tsvin:
        rent_reader = csv.reader(tsvin, delimiter=d)
        for line in rent_reader:
            try:
                insert_string = insert_string = "INSERT INTO rent_table (State, County, City, Mean_Cost, Median_Cost, Standard_Deviation) VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}');".format(line[2], line[4], line[5], line[15], line[16], line[17])
                cursor.execute(insert_string)
            except sqlite3.OperationalError:
                print(insert_string)



def create_table(cur):
    cur.execute("DROP TABLE rent_table;")
    cur.execute("CREATE TABLE IF NOT EXISTS rent_table (State TEXT, County TEXT, City TEXT, Mean_Cost REAL, Median_Cost REAL, Standard_Deviation REAL)")


conn = sqlite3.connect('rent.db')
cur = conn.cursor()
create_table(cur)
open_csv('rent_data.csv', cur)
conn.commit()
conn.close()
