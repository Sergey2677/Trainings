import openpyxl
import csv

book = openpyxl.open("example.xlsx", read_only=True)
sheet = book.active

with open("test.csv", "w", newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    for i in sheet:
        row = []
        for j in i:
            row.append(j.value)
        writer.writerow(row)
