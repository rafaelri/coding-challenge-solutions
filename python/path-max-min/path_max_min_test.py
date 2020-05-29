from path_max_min import maxPathScore, get_next, max_of_min
from hamcrest import *

#def test_max_min_path_3by3():
#    assert_that(maxPathScore([[7,5,3],[2,0,9],[4,5,9]]), equal_to(3))

def test_get_next_3by3_start():
    assert_that(list(get_next([[0,0,0],[0,0,0],[0,0,0]], (0,0), 3, 3)), equal_to([(0,1), (1,0)]))

def test_get_next_3by3_near_border():
    assert_that(list(get_next([[0,0,0],[0,0,0],[0,0,0]], (2,0), 3, 3)), equal_to([(2,1)]))


def test_max_of_min_3by3_on_border():
    assert_that(max_of_min([[0,0,0],[0,0,0],[0,0,0]], (2,3), 3, 3, 0), equal_to(0))
