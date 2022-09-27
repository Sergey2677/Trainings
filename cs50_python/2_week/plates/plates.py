def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
# Check lenght of vanity plates
    if len(s) < 2 or len(s) > 6:
        return False
# Check for first two characters is it not digital
    if s[0].isalpha() == False or s[1].isalpha() == False:
        return False
# Check for first zero
    i = 0
    while i < len(s):
        if s[i].isalpha() == False:
            if s[i] == '0':
                return False
            else:
                break
        i += 1
# Check for punctuation marks
    for c in s:
        if c in ['.', ' ', '!', '?']:
            return False
# Check for numbers in the middle string
    for i in range(len(s)):
        if s[i].isdigit():
            if not s[i:].isdigit():
                return False
# If we pass all the tests
    return True
main()