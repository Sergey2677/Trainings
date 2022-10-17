
# Declare a dict with keys and values of entrees
menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

# # Declare a variable sum of all dish prices
sum = 0.00

# Loop forever until press ctrl + d
while True:
    try:
        item = input("Item: ").title()
        # to Check whether item in dict with keys and values of dishes
        if item in menu:
            # to Calculate sum
            sum += menu[item]
            # to Print out total
            print("Total: ${:.2f}".format(sum))
    except EOFError:
        # Print out new line
        print()
        # Stop loop after press ctrl + d
        break