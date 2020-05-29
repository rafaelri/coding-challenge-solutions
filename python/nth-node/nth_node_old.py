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
        curr = head
        ctr = 0
        while curr and ctr < n:
            ctr = ctr + 1
            curr = curr.next
        trailing = head
        while curr:
            curr=curr.next
            trailing = trailing.next
        if trailing == head:
            if trailing.next:
                return trailing.next
            else:
                return None
        trailing.next = trailing.next.next
        return head

