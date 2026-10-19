class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        best = 0
        count = {}
        left = 0
        mfrq = 0
        for right in range(len(s)):
            count[s[right]] = 1 + count.get(s[right], 0)
            mfrq = max(mfrq, count[s[right]])
            while (right - left + 1) - mfrq > k:
                count[s[left]] -= 1
                left +=1
            best = max(right - left + 1, best)
        return best