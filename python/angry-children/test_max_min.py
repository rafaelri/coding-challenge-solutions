from max_min import maxMin
from hamcrest import *


def test_7_elements_k_3():
    assert_that(maxMin(3, [10,100,300, 200, 1000, 20, 30]), equal_to(20))

def test_3_elements_k_3():
    assert_that(maxMin(3, [10,20,30]), equal_to(20))