import Leapyear

def test_isLeapYear1():
    result = Leapyear.isLeapYear(2000)
    assert result == "2000 is a Leap Year."

def test_isLeapYear2():
    result = Leapyear.isLeapYear(1900)
    assert result == "1900 is not a Leap Year."

def test_isLeapYear3():
    result = Leapyear.isLeapYear(2001)
    assert result == "2001 is not a Leap Year."

def test_isLeapYear4():
    result = Leapyear.isLeapYear(2004)
    assert result == "2004 is a Leap Year."