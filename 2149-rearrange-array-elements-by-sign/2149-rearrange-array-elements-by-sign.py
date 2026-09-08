class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        res=[0]*n
        pos=0
        neg=1
        for i in range(n):
            if nums[i]<0:
                res[neg]=nums[i]
                neg+=2
                
            else:
                res[pos]=nums[i]
                pos+=2
        return res