# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution: 
    ##invariant: while list length is more than 1, merge incrementally
    ##helper merge function with two heads
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        def merge2_lists(head1, head2) -> Optional[ListNode]:
            res: Optional[ListNode] = None ##stores the head to return
            lst: Optional[ListNode] = None ##stores the built list
            ##both head1 and head2 got stuff
            while head1 is not None and head2 is not None:
                if head1.val <= head2.val:
                    if lst is None:
                        lst = head1
                        head1 = head1.next
                        res = lst
                    else:
                        lst.next = head1
                        head1 = head1.next
                        lst = lst.next
                else:
                    if lst is None:
                        lst = head2
                        res = lst
                        head2 = head2.next
                    else:
                        lst.next = head2
                        head2 = head2.next
                        lst = lst.next
            ##append the list
            if head1 is None:
                if lst is None:
                    lst = head2
                    return lst
                lst.next = head2
            elif head2 is None:
                if lst is None:
                    lst = head1
                    return lst
                lst.next = head1
            return res
        res: Optional[ListNode] = None

        #O(n k^2 solution, not the best). best is tournament bracket style), makes it log(k)
        while len(lists) > 1:
            merged_lists = []
            
            # Jump by 2 to grab pairs: (0,1), (2,3), (4,5)
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                # If there's an odd number of lists, the last one pairs with None
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                
                # Merge the pair and add to our new list for the next round
                merged_lists.append(merge2_lists(l1, l2))
                
            # Overwrite lists with the newly merged lists (halving the size)
            lists = merged_lists
            
        return lists[0]
