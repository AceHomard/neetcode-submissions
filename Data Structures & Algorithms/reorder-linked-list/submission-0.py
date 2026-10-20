# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def _splitinhalf(self, head: Optional[ListNode]) ->  Optional[ListNode]:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def _reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev

    def _merge_alternate(self, l1: Optional[ListNode], l2: Optional[ListNode]):
        while l1 and l2:
            tmp1 = l1.next
            tmp2 = l2.next
            l1.next = l2
            l2.next = tmp1
            l1 = tmp1
            l2 = tmp2

    def reorderList(self, head: Optional[ListNode]) -> None:
        mid = self._splitinhalf(head)
        h2 = mid.next
        mid.next = None
        h2 = self._reverseList(h2)
        self._merge_alternate(head, h2)