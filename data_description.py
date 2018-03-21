from raw_data import *

def number(data_sample):
    return len(data_sample) - 1


numb = number(data_from_csv)
print(numb)


def calculate_sum(data):
    data = []
    for row in data[1:]:
        data.append(row)
    return data

print(calculate_sum(data_from_csv))
