class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dis = [(x*x + y*y, [x,y]) for x, y in points]
        heapq.heapify(dis)
        res = [heapq.heappop(dis)[1] for _ in range(k)]
        return res
