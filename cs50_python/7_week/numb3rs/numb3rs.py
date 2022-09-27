#     #.#.#.# - each # should be from 0 up to 255
import re
import sys

# Main funct
def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    # Search for matches with pattern
    if re.search(r"^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$", ip):
        # If there is matches, split value with separate sign '.'
        split_ip = ip.split(".")
        # for each value in each octet
        for number in split_ip:
            # If value of any octet bigger than 255, return false
            if int(number) > 255:
                return False
        # If all octets is checked, return True
        return True
    # If there is no matches, return False
    else:
        return False

if __name__ == "__main__":
    main()