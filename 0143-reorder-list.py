# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next 
        slow.next = None
        prev = None
        while second:
            nxt = second.next
            second.next = prev 
            prev = second
            second = nxt 

        first, second = head, prev 
        while first and second:
            first_nxt = first.next 
            second_nxt = second.next
            first.next = second
            second.next = first_nxt
            first = first_nxt 
            second = second_nxt 


