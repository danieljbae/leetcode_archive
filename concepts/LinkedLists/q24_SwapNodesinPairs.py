# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        
        Analysis: Iterative approach
        - Time: O(n)
        - Space: O(1)
        """
        tmp = ListNode(-1)
        tmp.next = head
        
        prev = tmp
        
        while head and head.next:
            # nodes to be swapped
            first_node = head
            second_node = head.next
            
            # swap 
            prev.next = second_node # bridge old pair to current pair
            first_node.next = second_node.next 
            second_node.next = first_node
            
            # incrumenting to new pair
            prev = first_node # tail of old pair
            head = first_node.next # head of new pair  
        
        return tmp.next