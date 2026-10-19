class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        window = Counter()
        best_len = len(s) + 1
        res = ""
        l = 0
        need_count = len(need)
        have = 0
        for r in range(len(s)):
            window[s[r]] += 1
            if window[s[r]] == need[s[r]]:
                have += 1
            while have == need_count:
                if r - l + 1 < best_len:
                    res = s[l:r+1]
                    best_len = r - l + 1
                window[s[l]] -= 1
                if window[s[l]] < need[s[l]]:
                    have -= 1
                l += 1
        return res