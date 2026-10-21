# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def _length(self, head: Optional[ListNode]):
        i = 0
        while head:
            head = head.next
            i +=1
        return i

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy
        enindex = self._length(head) - n
        for _ in range(enindex):
            prev = prev.next
        prev.next = prev.next.next
        return dummy.next