class Solution:
    def twoSum(self, s, i, res):
        j, k = i + 1, len(s) - 1
        while j < k:
            som = s[i] + s[j] + s[k]
            if som > 0:
                k -= 1
            elif som < 0:
                j += 1
            else:
                res.append([s[i], s[j], s[k]])
                k -= 1
                j += 1
                while j < k and s[j] == s[j - 1]:
                    j += 1
        
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        s = sorted(nums)
        res = []
        for i in range(len(s)):
            if s[i] > 0:
                break
            if i > 0 and s[i] == s[i-1]:
                continue
            self.twoSum(s, i, res)
        return res