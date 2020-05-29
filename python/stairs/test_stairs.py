from hamcrest import *
from stairs import num_ways_paint
def test_single_stair():
    assert_that(num_ways_paint(1), equal_to(2))

def test_second_stair_prev_yellow():
    assert_that(num_ways_paint(1, 'y'), equal_to(1))    

def test_second_stair_prev_green():
    assert_that(num_ways_paint(1, 'g'), equal_to(2))        

def test_two_stairs():
    assert_that(num_ways_paint(2), equal_to(3))
