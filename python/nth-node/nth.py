from nth_node import ListNode, Solution
from nth_node_test import to_list

#n1 = ListNode(1)
#n2 = ListNode(2)
#n1.next = n2
#n3 = ListNode(3)
#n2.next = n3
#n4 = ListNode(4)
#n3.next = n4
#n5 = ListNode(5)
#n4.next = n5
#
#Solution().removeNthFromEnd(n1, 2)

n1 = ListNode(1)
n2 = ListNode(2)
n1.next = n2

print(to_list(Solution().removeNthFromEnd(n1, 1)))
