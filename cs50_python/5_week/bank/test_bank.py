from bank import value

# Test with full "hello"
def test_value_hello():
    assert value("Hello") == 0
    assert value("hELLO") == 0
    assert value("HELLO") == 0

# Test with only first "h"
def test_value_h():
    assert value("Holle") == 20
    assert value("hOLLE") == 20
    assert value("HOLLE") == 20

# Test with no "hello" and first "h"
def test_value_word():
    assert value("try") == 100
    assert value("Bye") == 100
    assert value("GOODBYE") == 100

# Test digit input
def test_value_digit():
    assert value("1234") == 100

# Test punctuation marks input
def test_value_punct():
    assert value("!") == 100
    assert value("?") == 100
    assert value(".") == 100
