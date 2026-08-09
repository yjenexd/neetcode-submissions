# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#fast and slow approach
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast,slow = head, head
        #while fast is not None
        while fast and fast.next:
            fast = fast.next.next #this necessitates a fast.next not none check
            slow = slow.next
            if fast == slow:
                return True
        return False

        