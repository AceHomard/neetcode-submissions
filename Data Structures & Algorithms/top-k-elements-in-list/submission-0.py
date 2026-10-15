class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = [x for x, _ in Counter(nums).most_common(k)]
        return res