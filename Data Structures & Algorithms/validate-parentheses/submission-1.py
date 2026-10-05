class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = dict()
        pairs["("] = ")"
        pairs["["] = "]"
        pairs["{"] = "}"

        for par in s:
            if par in pairs:
                stack.append(par)
            elif len(stack) == 0:
                return False
            elif par is not pairs[stack.pop()]:
                return False
        return len(stack) == 0