# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        prev, curr = None, head

        if head is None:
            return head
        
        while head:
            tmp = head.next
            head.next = prev
            prev = head
            head = tmp

        return prev 


        