def main():
    while True:
        x = input("Fraction: ")
        convert_result = convert(x)
        gauge_result = gauge(convert_result)
        print(gauge_result)

def convert(fraction):
    while True:
        try:
            # Try, is it possible to do split funct with separate sign "/" for input
            numerator, denominator = fraction.split("/")
            # Calculate result
            result = (int(numerator) / int(denominator))
            # Check is it really level of fuel or not, if yes, return value of result in percent
            if result <= 1:
                return round(result * 100)
            else:
                fraction = input("Fraction: ")
                pass
        # Raise erros
        except (ValueError, ZeroDivisionError):
            raise


def gauge(result):
    if result >= 99:
        return "F"
    elif result <= 1:
        return "E"
    else:
        return f"{result}%"


if __name__ == "__main__":
    main()
