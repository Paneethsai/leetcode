class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        x = sorted(set(nums))
        longest = 1
        current = 1
        
        for i in range(1, len(x)):
            if x[i] == x[i - 1] + 1:
                current += 1
            else:
                current = 1
            longest = max(longest, current)
            
        return longest