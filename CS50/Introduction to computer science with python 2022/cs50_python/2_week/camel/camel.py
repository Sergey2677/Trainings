# Prompt user for a camelCase text
camelCase = input("camelCase: ")

# Create an empty snake_case text
snake_case = ""

# Loop through camelCase text
for i in range(len(camelCase)):
    if camelCase[i].isupper():
        snake_case += '_' + camelCase[i].lower()
    else:
        snake_case += camelCase[i]

# Print result
print("snake_case:", snake_case)