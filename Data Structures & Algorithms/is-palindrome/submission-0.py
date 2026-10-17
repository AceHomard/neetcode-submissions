class Solution:
    def isPalindrome(self, s: str) -> bool:
        cop = "".join([c.lower() for c in s if c.isalnum()])
        left, right = 0, len(cop) - 1
        while left < right:
            if cop[left] != cop[right]:
                return False
            left += 1
            right -= 1
        return True