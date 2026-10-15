class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            y = target - nums[i]
            if y in d:
                return [d[y], i]
            d[nums[i]] = i
        return []