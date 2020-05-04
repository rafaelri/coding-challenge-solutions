from hamcrest import *
from running_median import RunningMedian

def test_single():
    r = RunningMedian()
    assert_that(r.add(12), equal_to(12))

def test_two_elements():
    r = RunningMedian()
    r.add(12)
    assert_that(r.add(4), equal_to(8))   

def test_two_elements_right():
    r = RunningMedian()
    r.add(4)
    assert_that(r.add(12), equal_to(8))   

def test_three_elements():
    r = RunningMedian()
    r.add(12)
    r.add(4)
    assert_that(r.add(5), equal_to(5))       

def test_four_elements():
    r = RunningMedian()
    r.add(12)
    r.add(4)
    r.add(5)
    assert_that(r.add(3), equal_to(4.5))       

def test_five_elements():
    r = RunningMedian()
    r.add(12)
    r.add(4)
    r.add(5)
    r.add(3)
    assert_that(r.add(8), equal_to(5))       

def test_six_elements_right():
    r = RunningMedian()
    r.add(12)
    r.add(4)
    r.add(5)
    r.add(3)
    r.add(8)
    assert_that(r.add(7), equal_to(6)) 

def test_six_elements_left():
    r = RunningMedian()
    r.add(4)
    r.add(5)
    r.add(3)
    r.add(6)
    r.add(8)
    assert_that(r.add(7), equal_to(5.5))     