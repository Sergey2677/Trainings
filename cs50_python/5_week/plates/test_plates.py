from plates import is_valid

# Max characters
def test_range_of_characters():
    assert is_valid('AB') == True
    assert is_valid('ASDSAD') == True
    assert is_valid('T') == False
    assert is_valid('SKAJFJAD') == False

# If first two characters is not letters
def test_starting_with_two_letters():
    assert is_valid('AA') == True
    assert is_valid('B1') == False
    assert is_valid('51') == False

# If in the middle of plates is digits
def test_numbers_in_middle():
    assert is_valid("AFS129") == True
    assert is_valid("AS23A") == False

# The first number used cannot be 0
def test_first_number_zero():
    assert is_valid("CS05") == False
    assert is_valid("CS50") == True
    assert is_valid("CS50E") == False

# No periods, spaces, or punctuation marks are allowed
def test_other_characters():
    assert is_valid("AS3!14") == False
    assert is_valid("CS 50") == False
    assert is_valid("Hello!") == False