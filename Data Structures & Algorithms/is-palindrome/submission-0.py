class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [letter.lower() for letter in s if letter.isalpha() or letter.isnumeric()] 

        i = 0
        j = len(s)-1
        

        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True