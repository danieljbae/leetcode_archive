class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        '''
        https://leetcode.com/problems/partition-labels/discuss/861875/Python-3-or-Two-Pointer-Hash-Table-O(N)-or-Explanation
        
        1) First pass, record last index of each char
        2) Second pass, update most right index, until current index i is same as right; add difference to ans
            - maintain the most left index of each segment (left)
        '''       
        last = {char:i for i,char in enumerate(S)}

        partitions = []
        left, right = -1, -1
        for i,char in enumerate(S):
            right = max(right,last[char])
            if i == right: # end of partition
                partitions.append(right - left)
                left = right
        
        return partitions
                
        
            