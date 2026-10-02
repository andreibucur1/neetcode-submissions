class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash = dict()
        for n in nums:
            if n not in hash:
                hash[n] = 1
            else:
                hash[n] += 1

        sort = sorted(hash.items(), key = lambda item: item[1], reverse=True)
        sol = []
        for elem in sort:
            if k == 0:
                break
            k -= 1
            sol.append(elem[0])
        return sol