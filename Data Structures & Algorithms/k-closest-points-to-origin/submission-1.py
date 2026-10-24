class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dis = [(p[0]**2 + p[1]**2, p) for p in points]
        heapq.heapify(dis)
        res = []
        for _ in range(k):
            _, point = (heapq.heappop(dis))
            res.append(point)
        return res