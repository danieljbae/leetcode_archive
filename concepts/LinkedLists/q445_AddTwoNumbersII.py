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
        """
        n1 = ""
        n2 = ""
        
        while l1 or l2:
            if l1:
                n1 += str(l1.val)
                l1 = l1.next
            if l2:
                n2 += str(l2.val)
                l2 = l2.next
        total = int(n1)+int(n2)
        
        # convert total into list
        ls = [int(char) for char in str(total)]
        
        head = ListNode(ls[0]) 
        cursor = head
        for num in ls[1:]:
            cursor.next = ListNode(num)
            cursor = cursor.next
        return head