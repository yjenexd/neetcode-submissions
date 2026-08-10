# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return

        # 1. Find the middle of the linked list using fast and slow pointers
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        # 2. Reverse the second half of the list
        # slow is currently at the mid-point. 
        # We start reversing from slow.next and sever the first half.
        curr = slow.next
        slow.next = None  # Crucial step: disconnect the first half!
        prev = None
        
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            
        # 3. Merge the two halves alternatingly
        first = head
        second = prev  # prev is the new head of the reversed second half
        
        while second:
            # Store next nodes
            tmp1, tmp2 = first.next, second.next
            
            # Link the nodes together
            first.next = second
            second.next = tmp1
            
            # Move pointers forward
            first = tmp1
            second = tmp2

        
    
        