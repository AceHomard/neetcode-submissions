class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        y = set()
        for n in nums:
            if n in y:
                return True
            y.add(n)
        return False