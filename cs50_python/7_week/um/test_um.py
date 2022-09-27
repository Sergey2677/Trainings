from um import count


def test_with_valid_string():
    assert count("um") == 1
    assert count("um umu umumumumu um") == 2
    assert count("UM Um UUM um MU um UMMM UM") == 5

def test_with_punct_marks():
    assert count("um?") == 1
    assert count("Um, thanks for the album.") == 1
    assert count("Um, thanks, um...") == 2

def test_without_words():
    assert count("1234") == 0
    assert count("!,>") == 0
    assert count("12um12") == 0