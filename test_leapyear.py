import unittest
import Leapyear

class test_Cases(unittest.TestCase):
    def test_isLeapYear1(self):
        self.assertEqual(Leapyear.isLeapYear(2000), "2000 is a Leap Year.")

    def test_isLeapYear2(self):
        self.assertEqual(Leapyear.isLeapYear(1900), "1900 is not a Leap Year.")

    def test_isLeapYear3(self):
        self.assertEqual(Leapyear.isLeapYear(2001), "2001 is not a Leap Year.")

    def test_isLeapYear4(self):
        self.assertEqual(Leapyear.isLeapYear(2004), "2004 is a Leap Year.")

if __name__ == '__main__':
    unittest.main()