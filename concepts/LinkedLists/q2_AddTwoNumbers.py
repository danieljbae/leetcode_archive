# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
         
        Analysis: Iterative
        - time: O(n)
        - space: O(3n?)
        """
        stack1 = [] # || O(2n) space
        stack2 = []
        cur1, cur2 = l1, l2
        
        # Add each num in non-reverse order, as a str to concatenate || O(n) time 
        while cur1 or cur2:
            if cur1:
                stack1.insert(0,str(cur1.val))
                cur1 = cur1.next
                
            if cur2:
                stack2.insert(0,str(cur2.val))
                cur2 = cur2.next
        
        # Concatenate + Convert back to integer to calc sum || O(n) 
        n1 = int("".join(stack1))
        n2 = int("".join(stack2))
        total = n1 + n2
        
        # Convert each num of the total, as a element in list || O(n) time and space
        ls  = [int(char) for char in str(total)]
        
        # Add each element in list as a node in Linked List || O(n)
        head = ListNode()
        curr = head
        for i in range(len(ls)-1,-1,-1):
            curr.next = ListNode(ls[i]) 
            curr = curr.next
        
        return head.next # Return head