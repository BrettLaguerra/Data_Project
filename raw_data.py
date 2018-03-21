import csv
import sqlite3
import numpy


def open_with_csv(filename, cursor, d=','):
    data = []
    #open sqlite
    with open(filename) as tsvin:
        rent_reader = csv.reader(tsvin, delimiter=d)
        cv = 0
        for line in rent_reader:
            if cv > 0:
                try:
                    insert_string = "INSERT INTO rent_table (State, County, City, Mean_Cost, Median_Cost, Standard_Deviation) VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}');".format(line[2], line[4], line[5], line[15], line[16], line[17])
                    cursor.execute(insert_string)
                else:
                    print(insert_string)
            cv += 1
        return data


def create_table(cur):
    cur.execute("DROP TABLE rent_table;")
    cur.execute("CREATE TABLE IF NOT EXISTS rent_table (State TEXT, County TEXT, City TEXT, Mean_Cost REAL, Median_Cost REAL, Standard_Deviation REAL)")
#FIELDNAMES = ['id', 'State_Code', 'State_Name', 'State_ab', 'County', 'City', 'Place', 'Type', 'Primary', 'Zip_Code', 'Area_Code', 'ALand', 'AWater', 'Lat', 'Lon', 'Mean', 'Median', 'Stdev', 'Samples']


def average_rent(cur):
    cur.execute("SELECT ROUND(AVG(Mean_Cost)) FROM rent_table WHERE State = 'Alabama'")


conn = sqlite3.connect('rent.db')
cur = conn.cursor()
#step 1: create_table(cur)
open_with_csv('rent_data.csv', cur)
conn.commit()
cur.close()
