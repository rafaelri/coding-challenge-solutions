from first_missing_int import Solution
from hamcrest import *

def test_three_items_with_one_zero():
    assert_that(Solution().firstMissingPositive([3,2,0]), equal_to(1))
def test_three_items_with_one_zero2():
    assert_that(Solution().firstMissingPositive([1,2,0]), equal_to(3))    
def test_huge_items():
    assert_that(Solution().firstMissingPositive([7,8,9,11,12]), equal_to(1))    
def test_empty_list():
    assert_that(Solution().firstMissingPositive([]), equal_to(1))    
def test_next_item_list():
    assert_that(Solution().firstMissingPositive([4,3,2,1]), equal_to(5))    
def test_next_item_list_in_order():
    assert_that(Solution().firstMissingPositive([1,2,3,4]), equal_to(5))    
def test_item_collide_out_of_range():
    assert_that(Solution().firstMissingPositive([1,1000]), equal_to(2))    
def test_item_duplicate():
    assert_that(Solution().firstMissingPositive([1,1]), equal_to(2))
def test_long_input():
    assert_that(Solution().firstMissingPositive([10,4,16,54,17,-7,21,15,25,31,61,1,6,12,21,46,16,56,54,12,23,20,38,63,2,27,35,11,13,47,13,11,61,39,0,14,42,8,16,54,50,12,-10,43,11,-1,24,38,-10,13,60,0,44,11,50,33,48,20,31,-4,2,54,-6,51,6]), equal_to(100))    
    