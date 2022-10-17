from twttr import shorten

def test():
    assert shorten('pink') == 'pnk'
    assert shorten('RED') == 'RD'
    assert shorten('OrAnGe') == 'rnG'
    assert shorten("Twitter") == "Twttr"
    assert shorten("What's your name?") == "Wht's yr nm?"
    assert shorten("CS50") == "CS50"
