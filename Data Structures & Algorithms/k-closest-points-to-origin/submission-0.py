class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        mh = []

        for x, y in points:
            dist = (x ** 2 + y ** 2)
            mh.append([dist, x, y])
            
        heapq.heapify(mh)
        print(mh)
        res = []
        while k > 0:
            dist, x, y = heapq.heappop(mh)
            res.append([x, y])
            k -= 1

        return res