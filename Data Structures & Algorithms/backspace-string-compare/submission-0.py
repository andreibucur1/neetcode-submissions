class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1 = []
        stack2 = []
        for l in s:
            if l == "#":
                if stack1:
                    stack1.pop()
            else:
                stack1.append(l)
        for l in t:
            if l == "#":
                if stack2:
                    stack2.pop()
            else:
                stack2.append(l)
        return stack1 == stack2
