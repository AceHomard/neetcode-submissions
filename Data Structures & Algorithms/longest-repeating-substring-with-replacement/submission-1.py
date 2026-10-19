class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        letters = set(s)
        best = 0
        for letter in letters:
            left = 0
            cost = 0
            for right in range(len(s)):
                if s[right] != letter:
                    cost += 1
                while cost > k:
                    if s[left] != letter:
                        cost -= 1
                    left += 1
                best = max(right - left + 1, best)
        return best