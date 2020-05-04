from nth_node import ListNode, Solution
from hamcrest import *

def to_list(head: ListNode):
    res = list()
    curr = head
    while curr:
        res.append(curr.val)
        curr=curr.next
    return res

def test_single_node_remove_first_from_last():
    n1 = ListNode(1)
    assert_that(Solution().removeNthFromEnd(n1, 1), equal_to(None))

    
def test_single_first_sample_return_2_from_5():
    n1 = ListNode(1)
    n2 = ListNode(2)
    n1.next = n2
    n3 = ListNode(3)
    n2.next = n3
    n4 = ListNode(4)
    n3.next = n4
    n5 = ListNode(5)
    n4.next = n5
    assert_that(to_list(Solution().removeNthFromEnd(n1, 2)), equal_to(list([1, 2, 3, 5])))

def test_single_first_sample_return_5_from_5():
    n1 = ListNode(1)
    n2 = ListNode(2)
    n1.next = n2
    n3 = ListNode(3)
    n2.next = n3
    n4 = ListNode(4)
    n3.next = n4
    n5 = ListNode(5)
    n4.next = n5
    assert_that(to_list(Solution().removeNthFromEnd(n1, 5)), equal_to(list([2, 3, 4, 5])))    

def test_single_first_sample_return_1_from_2():
    n1 = ListNode(1)
    n2 = ListNode(2)
    n1.next = n2
    assert_that(to_list(Solution().removeNthFromEnd(n1, 1)), equal_to(list([1])))        