from sys import argv, exit
import csv
from tabulate import tabulate

# Check argv value
if len(argv) > 2:
    print("Too many command-line arguments")
    exit(1)
elif len(argv) < 2:
    print("Too few command-line arguments")
    exit(1)
elif argv[1][(len(argv[1]) - 4):] != '.csv':
    print("Not a CSV file")
    exit(1)
else:
    # Create a list of items that were loaded from a csv file
    list_of_items = []
    try:
        # Try open file that entered by user to comand-line
        with open(f"{argv[1]}", 'r') as file:
            reader = csv.reader(file)
            # Convert items from file csv to list of files
            for i in reader:
                list_of_items.append(i)
    # If an error has occurred
    except FileNotFoundError:
        print("File does not exist")
        exit(1)


# Create headers
headers = list_of_items[0]
# Create table's items
table  = list_of_items[1:]
# Print out the tesult
print(tabulate(table, headers, tablefmt="grid"))
