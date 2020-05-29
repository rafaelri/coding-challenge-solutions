from zombie_infection import humanDays, get_rows, adjacents, infect
from hamcrest import *

def test_sample(): 
    initial = [[0, 1, 1, 0, 1], \
               [0, 1, 0, 1, 0], \
               [0, 0, 0, 0, 1], \
               [0, 1, 0, 0, 0]]
    assert_that(humanDays(initial), equal_to(2))

def test_adjacents_corner_start():
    assert_that(adjacents((0,0), 2, 2), equal_to([(1,0),(0,1)]))

def test_adjacents_corner_end():
    assert_that(adjacents((0,1), 2, 2), equal_to([(0,0),(1,1)]))