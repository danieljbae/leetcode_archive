class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        
        d = set(arr)
        for i in range(len(arr)):
            if (2 * float(arr[i])) in d and arr.index(2 * float(arr[i]))!=i:
                return True
        
        return False