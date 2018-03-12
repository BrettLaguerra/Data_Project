import csv
import numpy

def open_with_csv(filename, d=','):
    data = []
    with open(filename) as tsvin:
        rent_reader = csv.reader(tsvin, delimiter=d)
        for line in rent_reader:
            data.append(line)
    return data


FIELDNAMES = ['id', 'State_Code', 'State_Name', 'State_ab', 'County', 'City', 'Place', 'Type', 'Primary', 'Zip_Code', 'Area_Code', 'ALand', 'AWater', 'Lat', 'Lon', 'Mean', 'Median', 'Stdev', 'Samples']

data_from_csv = open_with_csv('rent_data.csv')


def load_data(filename, d=','):
    my_csv = numpy.genfromtxt(filename, delimiter=d, skip_header=1, invalid_raise=False, names=FIELDNAMES)
    return my_csv
