class Solution:
    def removeStars(self, s: str) -> str:
        """
        For Loop over the input string 
            if char != "*":
                stack.append(char)
            else:
                stack.pop()
        return str(stack)

                  i
        "leet**cod*e"

        [l,e,c,o,e]

        """
        stack = []
        for char in s:
            if char == "*" and stack:
                stack.pop()
            else:
                stack.append(char)
                
        
        return "".join(stack) if stack else ""