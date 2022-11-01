from sys import argv, exit
import csv

# Check argv value
if len(argv) > 3:
    print("Too many command-line arguments")
    exit(1)
elif len(argv) < 2:
    print("Too few command-line arguments")
    exit(1)
elif ".csv" not in argv[1] or ".csv" not in argv[2]:
    print("Not a CSV file")
    exit(1)
else:
    try:
        before = []
        with open(f"{argv[1]}", 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                first, last = row['name'].split(',')
                before.append({"first": last.strip(), "last": first, "house": row["house"]})
    except FileNotFoundError:
        print(f"Could not read {argv[1]}")
        exit(1)

with open(f"{argv[2]}", "w") as file1:
    writer = csv.DictWriter(file1, fieldnames=["first", "last", "house"])
    writer.writerow({"first": "first", "last": "last", "house": "house"})
    for row in before:
        writer.writerow({"first": row["first"], "last": row["last"], "house": row["house"]})