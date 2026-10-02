class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1

        while i != j:
            suma = numbers[i] + numbers[j]
            if suma == target:
                return [i+1, j+1]
            elif suma > target:
                j -= 1
            else:
                i += 1

        return 0