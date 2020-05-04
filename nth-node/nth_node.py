import math
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    def __repr__(self):
        return self.val
    def __str__(self):
        return self.val
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        base = ListNode(math.inf)
        base.next = head
        curr = base
        ctr = 0
        while curr and ctr < n:
            ctr = ctr + 1
            curr = curr.next
        trailing = base
        while curr.next:
            curr=curr.next
            trailing = trailing.next
        trailing.next = trailing.next.next
        return base.next

