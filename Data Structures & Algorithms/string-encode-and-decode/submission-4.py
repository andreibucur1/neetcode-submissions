class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""

        for str1 in strs:
            string += '@'
            string += str(len(str1))
            string += '@'
            string += str1

        return string
    def decode(self, s: str) -> List[str]:
        response = []
        i = 0

        while i < len(s):
            j = i + 1
            while s[j] != '@':
                j += 1

            length = int(s[i+1:j])
            word = s[j + 1:j + length + 1]
            i = j + length + 1
            response.append(word)

        return response