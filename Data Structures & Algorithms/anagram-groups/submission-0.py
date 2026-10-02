class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash = dict()
        for s in strs:
            ordered_str = "".join(sorted(s))
            if ordered_str not in hash:
                hash[ordered_str] = [s]
            else:
                hash[ordered_str].append(s)

        sol = []
        for value in hash.values():
            sol.append(value)

        return sol