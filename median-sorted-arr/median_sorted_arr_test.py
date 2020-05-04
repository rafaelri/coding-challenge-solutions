from median_sorted_arr import Solution
from hamcrest import *

def test_arr_3_entries():
    assert_that(Solution().findMedianSortedArrays([1,3],[2]), equal_to(2.0))
def test_arr_4_entries():
    assert_that(Solution().findMedianSortedArrays([1,2],[3,4]), equal_to(2.5))