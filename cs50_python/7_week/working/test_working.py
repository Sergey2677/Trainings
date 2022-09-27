from working import convert
import pytest


# Test valid input
def test_1():
    assert convert('11 AM to 7 PM') == '11:00 to 19:00'
    assert convert('12 AM to 3 PM') == '00:00 to 15:00'
    assert convert('10:30 PM to 8:50 AM') == '22:30 to 08:50'


def test_2():
    with pytest.raises(ValueError):
        convert("3:70 PM to 13:80 AM")
    with pytest.raises(ValueError):
        convert("3PM to 11AM")
    with pytest.raises(ValueError):
        convert("3PM 11AM")
    with pytest.raises(ValueError):
        convert("03:00 to 11:30")


if __name__ == "__main__":
    main()