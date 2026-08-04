class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        x=set(nums)
        max_=max(nums)
        min_=min(nums)
        miss=[]
        for i in range(min_,max_):
            if i not in x:
                miss.append(i)
        return miss