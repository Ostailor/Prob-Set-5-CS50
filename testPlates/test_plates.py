from testPlates.plates import is_valid


def test_check_zero_last():
    assert is_valid('CS50') == True


def test_check_zero_first():
    assert is_valid('CS05') == False


def test_check_numbers():
    assert is_valid("CS50P") == False


def test_check_letters():
    assert is_valid("PI3.14") == False


def test_check_beginning():
    assert is_valid("50CS") == False


def test_check_length():
    assert is_valid("cscscscs") == False