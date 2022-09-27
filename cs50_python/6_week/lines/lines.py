from sys import argv, exit

# Check argv value
if len(argv) > 2:
    print("Too many command-line arguments")
    exit(1)
elif len(argv) < 2:
    print("Too few command-line arguments")
    exit(1)
elif argv[1][(len(argv[1]) - 3):] != '.py':
    print("Expected non-zero exit code")
    exit(1)
else:
    # Create copy file without whitespace lines and comments
    copy_file = []
    # Try open file with argv value
    try:
        with open(f"{argv[1]}", 'r') as file:
            for row in file:
                # Check is it totally whitespase row or not
                if not row.isspace():
                    # Strip whitespaces
                    row = row.strip()
                    # Check, is the row starts with hash sign
                    if not row.startswith('#'):
                        # If all checks passed, append to copy file
                        copy_file.append(row)
    except:
        print("File does not exist")
        exit(1)

# To count value of lenght of file
counter = 0
for item in copy_file:
        counter += 1
# Print out the result
print(counter)


