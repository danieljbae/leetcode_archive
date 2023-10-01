class Solution(object):
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        print(str)
        
        out = ""
        for i in range(len(str)):
            c = str[i]
            pre = ord(c)
            
            if pre < 90 and c.isalpha():
                post = pre + 32
                out += chr(post)
            else:
                out += c
            
            
        return out
            
            
        