class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dis = []
        for p in points:
            dis.append((p[0]**2 + p[1]**2, p))
        heapq.heapify(dis)
        res = []
        for _ in range(k):
            _, point = (heapq.heappop(dis))
            res.append(point)
        return res