# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cursor = head
        while cursor and cursor.next:
            if cursor.next.val == cursor.val:
                cursor.next = cursor.next.next
            else:
                cursor = cursor.next
                
        return head
        