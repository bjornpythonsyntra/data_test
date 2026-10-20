import csv
from tabulate import tabulate

with open("university_records.csv", "r") as f:
    data_list = []
    data = csv.reader(f)
    for row in data:
        data_list.append(row)

print(tabulate(data_list[1:],headers=data_list[0]))