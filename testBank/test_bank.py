from testBank.bank import value


def test_check_hello():
    assert value('Hello') == "$0"


def test_check_h():
    assert value("Hi") == "$20"


def test_check_lowercase():
    assert value("What's up? Homie") == "$100"
