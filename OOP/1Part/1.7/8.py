import re

class CardCheck:

    @staticmethod
    def check_card_number(number):
        if matches := re.search(
                r'^\d{4}-\d{4}-\d{4}-\d{4}$', number):
            return True
        return False

    @staticmethod
    def check_name(name):
        if matches := re.search(
                r'^[a-zA-Z0-9]+\s[a-zA-Z0-9]+$', name):
            return True
        return False


is_number = CardCheck.check_card_number("1234-5678-9012-1000")
is_name = CardCheck.check_name("SERGEI BALAKIREV")


print(is_number)
print(is_name)
