# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        heap = []

        for i in range(len(lists)):
            while lists[i] is not None:
                heappush(heap, lists[i].val)
                lists[i] = lists[i].next
                
        while heap:
            node = ListNode(heappop(heap))
            curr.next = node
            curr = curr.next 
        
        return dummy.next
