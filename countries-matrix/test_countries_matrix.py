from hamcrest import *
from countries_matrix import count_countries

def test_5by5_3_countries():
    m = [ \
          [1,1,2,1,1], \
          [1,1,2,1,1], \
          [1,1,2,1,1], \
          [1,1,2,1,1], \
          [1,1,2,1,1], \
        ]
    assert_that(count_countries(m), equal_to(3))

def test_5by5_other_3_countries():
    m = [ \
          [1,1,2,1,1], \
          [1,1,2,1,1], \
          [1,1,1,1,1], \
          [1,1,2,1,1], \
          [1,1,2,1,1], \
        ]
    assert_that(count_countries(m), equal_to(3))

def test_5by5_2_countries():
    m = [ \
          [1,1,2,1,1], \
          [1,1,2,1,1], \
          [1,1,2,1,1], \
          [1,1,2,1,1], \
          [1,1,1,1,1], \
        ]
    assert_that(count_countries(m), equal_to(2))    