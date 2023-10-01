class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        
        Analysis:
        Time - O(n), stack push/pop is O(1)
        Space - O(n), hashmap is fixed and w.c. stack is O(n) ie s is all closing brackets 
        """
        if len(s) == 0 or len(s)%2 != 0: # Base: empty or odd len
            return False

        stack = []
        
        closing = {
            "]": "[",
            ")": "(",
            "}": "{"
        }
        
        for char in s:    
            if char in closing.keys():                
                if not stack or closing[char] != stack.pop(): # closing brackets before opening 
                    return False
            else:
                stack.append(char)
                
        return len(stack) == 0