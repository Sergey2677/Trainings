# main funct
def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

# Cut dollar sign and convert to float from str
def dollars_to_float(d):
    d_without_dollar_sign = d.replace("$", "")
    return float(d_without_dollar_sign)

# Cut percent sign and convert
def percent_to_float(p):
    p_without_percent_sign = p.replace("%", "")
    p_converted = float(p_without_percent_sign) / 100
    return p_converted

# Call main funct
main()