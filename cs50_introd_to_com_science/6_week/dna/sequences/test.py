# AGATC,TTTTTTCT,AATG,TCTAG,GATA,TATC,GAAA,TCTG
import csv
import re

with open("18.txt") as file:
    text = file.read()
match = re.findall("AGATC", text )
print(len(match))