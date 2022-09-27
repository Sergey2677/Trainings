

# The main function
def main():
    # Assign result to variable
    result = calculate_fuel()
    # Print result
    if result >= 99:
        print("F")
    elif result <= 1:
        print("E")
    else:
        print(f"{result}%")

# Function which created for calculate fuel
def calculate_fuel():
    while True:
        # Ask user for input value
        x = input("Fraction: ")
        try:
            # Try, is it possible to do split funct with separate sign "/" for input
            numerator, denominator = x.split("/")
            # Calculate result
            result = (int(numerator) / int(denominator))
            # Check is it really level of fuel or not, if yes, return value of result in percent
            if result <= 1:
                return round(result * 100)
        except (ValueError, ZeroDivisionError):
            # Skip error messages
            pass

# Execute the main function
main()