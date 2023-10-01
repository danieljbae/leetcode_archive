# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        
        Analysis: 2-pointer approach
        O(n) - time
        O(n) - space
        """
        slow,fast = head, head
        while fast and fast.next:
            
            if fast.next is None: # reached end
                return False
            
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast: # cycle found as hare is equal tourtoise
                return True
            
                
        
        
        