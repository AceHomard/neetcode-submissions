class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        inverte = [-n for n in stones]
        heapq.heapify(inverte)
        while len(inverte) > 1:
            x = -heapq.heappop(inverte)
            y = -heapq.heappop(inverte)
            if x > y:
                heapq.heappush(inverte, -(x - y))
        return -inverte[0] if inverte else 0

                