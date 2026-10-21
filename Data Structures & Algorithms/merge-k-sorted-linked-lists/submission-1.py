# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        mini = []
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(mini, (node.val, i, node))
        while mini:
            _, i, node = heapq.heappop(mini)
            tail.next = node
            if node.next:
                heapq.heappush(mini, (node.next.val, i, node.next))
            tail = tail.next
        return dummy.next