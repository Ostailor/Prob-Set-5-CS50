from testTwttr.twttr import shorten


def test_check_uppercase():
    assert shorten('ALPHABET') == "LPHBT"


def test_check_lowercase():
    assert shorten("hello, world") == "hll, wrld"


def test_numbers():
    assert shorten('Hello2') == 'Hll2'
