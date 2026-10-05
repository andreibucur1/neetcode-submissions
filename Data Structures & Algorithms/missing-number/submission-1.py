class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s = 0
        n = len(nums)
        for num in nums:
            s += num
        return int(n*(n+1) / 2 - s)