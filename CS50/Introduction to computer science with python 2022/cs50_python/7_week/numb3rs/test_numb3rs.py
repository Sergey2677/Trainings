from numb3rs import validate


# Checking a valid range of input
def test_ip_range_true():
    assert validate("255.255.255.255") == True
    assert validate("0.0.0.0") == True
    assert validate("1.2.3.4") == True


# Checking an invalid range of input
def test_ip_range_false():
    assert validate("256.255.255.255") == False
    assert validate("255.300.255.255") == False
    assert validate("-1.255.255.255") == False


# Checking an invalid input value
def test_ip_input_word():
    assert validate("cat.255.255.255") == False
    assert validate("255.rat.255.255") == False
    assert validate("255.255.dog.255") == False


# Checking an invalid input separate signs
def test_ip_error_separate_sign():
    assert validate("255/255.255.255") == False
    assert validate("255.255!255.255") == False
    assert validate("255.255.dog)255") == False