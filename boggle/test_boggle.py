from hamcrest import *
from boggle import get_starts, get_next, is_word
default_boggle = [ ['G', 'I', 'Z'],
                   ['U', 'E', 'K'],
                   ['Q', 'S', 'E'] ]
def test_get_starts_single():
    assert_that(get_starts(default_boggle, 'Q'), equal_to([(2,0)]))

def test_get_starts_multiple():
    assert_that(get_starts(default_boggle, 'E'), equal_to([(1,1),(2,2)]))    

def test_get_starts_none():
    assert_that(get_starts(default_boggle, 'A'), equal_to([]))

def test_get_next_single_none_visited():
    visited = [ [0]*3 for i in range(3) ]
    assert_that(get_next(default_boggle, visited, (2,0), 'S'), equal_to([(2,1)]))    

def test_get_next_single_one_visited():
    visited = [ [0]*3 for i in range(3) ]
    visited[1][1]=1
    assert_that(get_next(default_boggle, visited, (2,1), 'E'), equal_to([(2,2)]))    

def test_is_word_inside():
    assert_that(is_word(default_boggle, 'GEEK'), equal_to(True))

def test_is_word_not_inside():
    assert_that(is_word(default_boggle, 'QUEEN'), equal_to(False))