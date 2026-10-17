class Solution:
    def isPalindrome(self, s: str) -> bool:
        cop = "".join([c.lower() for c in s if c.isalnum()])
        return cop == cop[::-1]
