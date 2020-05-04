from single_digit_dates import SingleDigitDates
from hamcrest import *
from datetime import date
def test_valid_valid():
    d = date(11,1,1)
    s = SingleDigitDates(d)
    assert_that(s.valid(), equal_to(True))

def test_valid_invalid():
    d = date(12,1,1)
    s = SingleDigitDates(d)
    assert_that(s.valid(), equal_to(True))
    assert_that(s.date, equal_to(date(22,2,2)))

def test_next_moves_to_next_valid():
    d = date(12,1,1)
    s = SingleDigitDates(d)
    assert_that(s.valid(), equal_to(True))
    assert_that(s.next(), equal_to(date(22,2,2)))
    
    assert_that(s.next(), equal_to(date(22,2,22)))
