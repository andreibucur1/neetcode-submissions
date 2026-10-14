class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nx2_plus_k = sum(nums)
        n_plus_k = sum(set(nums))
        n = nx2_plus_k - n_plus_k
        k = n_plus_k - n
        return k

