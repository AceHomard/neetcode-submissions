class Solution:
    def best_for(self, s, letter, k):
        left = 0
        cost = 0
        best = 0
        for right in range(len(s)):
            if s[right] != letter:
                cost += 1
            while cost > k:
                if s[left] != letter:
                    cost -= 1
                left += 1
            best = max(right - left + 1, best)
        return best

    def characterReplacement(self, s: str, k: int) -> int:
        letters = set(s)
        best = 0
        for letter in letters:
            best = max(self.best_for(s, letter, k), best)
        return best