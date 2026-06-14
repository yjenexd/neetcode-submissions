# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool: ##pass Optional parameter to ListNode object
        ##head is either a listNode object, or none,
        if head is None:
            return False
        seen = set()
        curr_node = head
        while curr_node.next is not None:
            if curr_node.next in seen:
                return True
            seen.add(curr_node)
            curr_node = curr_node.next
        return False
            
        