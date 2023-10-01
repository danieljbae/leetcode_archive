# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        Recursive Apporach
        
        Analysis
        Time: O(n)
        Space: O(n), n recursion stacks 
        """
        if head is None or head.next is None:
            return head 
        
        rev_head = self.reverseList(head.next)
        head.next.next = head # Reverse connection
        head.next = None # Fix/update old connection
        print(rev_head.val)
        return rev_head        
        
        

            
  