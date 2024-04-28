# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        prev = dummy 
        curr = head
        while True:
            nextNode = self.nextFinder(curr, k)
            if nextNode == False:
                if curr:
                    prev.next = curr
                return dummy.next
            prev.next = self.helper(curr, k)
            prev = curr
            curr = nextNode

    def nextFinder(self, curr, k):
        n = k 
        while n > 0 and curr:
            curr = curr.next
            n -= 1 
        if n == 0:
            return curr
        else:
            return False

    def helper(self, curr, k):
        n = k 
        prev = None
        while n > 0 and curr:
            nxt = curr.next
            curr.next = prev 
            prev = curr
            curr= nxt
            n -= 1 
        if n == 0:
            return prev
        else:
            return 


