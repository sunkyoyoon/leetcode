# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        prev,curr = dummy, head

        while curr and curr.next:
            temp = curr.next 
            nxt = temp.next
            prev.next = temp
            temp.next = curr 
            curr.next = nxt
            prev = curr
            curr = curr.next
            
        return dummy.next

