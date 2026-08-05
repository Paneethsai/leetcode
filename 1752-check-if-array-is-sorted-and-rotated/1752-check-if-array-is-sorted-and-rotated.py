class Solution:
    def check(self, nums: List[int]) -> bool:
        sort=sorted(nums)
        if nums== sort:
            return True
        n=len(nums)
        for i in range(n):
            if sort[i:] + sort[:i] == nums:
                return True
        return False