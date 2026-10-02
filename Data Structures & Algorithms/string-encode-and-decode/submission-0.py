class Solution:

    def encode(self, strs: List[str]) -> str:
        message = ""
        for word in strs:
            message += str(len(word)) + "#" + word
        return message
    def decode(self, s: str) -> List[str]:
        ans = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            l = int(s[i:j])
            word = s[j+1: j+1+l] 
            ans.append(word)
            i = j + 1 + l
        return ans
