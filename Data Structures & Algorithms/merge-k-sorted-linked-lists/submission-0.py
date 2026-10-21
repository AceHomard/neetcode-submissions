# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def _mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        merg = dummy
        while list1 and list2:
            if list1.val < list2.val:
                merg.next = list1
                list1 = list1.next 
            else:
                merg.next = list2
                list2 = list2.next
            merg = merg.next
        merg.next = list1 or list2
        return dummy.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        while len(lists) > 1:
            tmp = list()
            for x in range(0, len(lists), 2):
                y = lists[x + 1] if x + 1 < len(lists) else None
                tmp.append(self._mergeTwoLists(lists[x], y))
            lists = tmp
        return lists[0] if lists else None