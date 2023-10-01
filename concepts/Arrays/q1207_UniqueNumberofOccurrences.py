class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        unique = set(arr)
        element_occurences = []
        
        for el in unique: 
            if arr.count(el) in element_occurences:
                return False
            else:
                element_occurences.append(arr.count(el))
        return True
    