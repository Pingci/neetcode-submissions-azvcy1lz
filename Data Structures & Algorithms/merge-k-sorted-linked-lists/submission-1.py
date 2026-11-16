# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        while len(lists) > 1:
            merged = []

            for i in range(0, len(lists), 2):
                first = lists[i]
                second = lists[i + 1] if i + 1 < len(lists) else None
                merged.append(self.mergeTwoLists(first, second))

            lists = merged

        return lists[0]

    def mergeTwoLists(self, first, second):
        dummy = ListNode()

        tail = dummy

        while first and second:
            if first.val <= second.val:
                tail.next =  first
                first = first.next

            else:
                tail.next = second
                second = second.next

            tail = tail.next

        tail.next = first if first else second
        return dummy.next


