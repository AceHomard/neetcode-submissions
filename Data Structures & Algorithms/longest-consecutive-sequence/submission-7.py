class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = sorted(nums)
        best = 1 if nums else 0

        j = 1
        for i in range (len(s) - 1):
            if s[i+1] - 1 == s[i]:
                j += 1
            elif s[i+1] == s[i]:
                pass
            else:
                j = 1
            if j > best:
                best = j
        return best