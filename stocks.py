import csv
import time


api_rows = []
with open('30DayByMinute.csv') as file:
    csv_reader = csv.reader(file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        api_rows.append(row)
        line_count += 1

    print(api_rows[5)
