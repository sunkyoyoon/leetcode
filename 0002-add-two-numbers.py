# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l3 = ListNode()
        dummy = l3
        left = 0 
        while l1 and l2:
            if l1.val + l2.val + left >= 10:
                l3.val = (l1.val + l2.val + left) % 10 
                left = 1 
            elif l1.val + l2.val + left < 10:
                l3.val = (l1.val + l2.val + left) % 10 
                left = 0 
            l1 = l1.next
            l2 = l2.next
            if l1 or l2:
                l3.next = ListNode()
                l3 = l3.next
        
        while l1: 
            if l1.val + left >= 10: 
                l3.val = (l1.val + left) % 10
                left = 1 
            elif l1.val + left <= 10:
                l3.val = (l1.val + left) % 10
                left = 0 
            l1 = l1.next 
            if l1:
                l3.next = ListNode() 
                l3 = l3.next   

        while l2: 
            if l2.val + left >= 10: 
                l3.val = (l2.val + left) % 10
                left = 1 
            elif l2.val + left <= 10:
                l3.val = (l2.val + left) % 10
                left = 0 
            l2 = l2.next 
            if l2:
                l3.next = ListNode() 
                l3 = l3.next  

        if left:
            l3.next = ListNode() 
            l3 = l3.next 
            l3.val = 1
        return dummy
        

