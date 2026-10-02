class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i, v in enumerate(nums):
            wanted_num = target - v

            if wanted_num in hashmap:
                return [hashmap[wanted_num], i]

            hashmap[v] = i