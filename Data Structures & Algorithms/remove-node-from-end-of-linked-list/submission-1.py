# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy_node = ListNode(0, head)
        pointer = head
        #move pointer n steps ahead of dummy pointer
        while n != 0:
            pointer = pointer.next
            n -= 1
        while pointer is not None:
            pointer = pointer.next
            dummy_node = dummy_node.next
        #remove the node
        if dummy_node.next is head:
            return head.next
        dummy_node.next = dummy_node.next.next
        return head
            
        