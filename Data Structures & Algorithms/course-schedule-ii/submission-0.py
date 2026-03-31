from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        indeg = [0] * numCourses

        for course, pre in prerequisites:
            graph[pre].append(course)
            indeg[course] += 1

        q = deque([i for i in range(numCourses) if indeg[i] == 0])
        order = []

        while q:
            pre = q.popleft()
            order.append(pre)
            for nxt in graph[pre]:
                indeg[nxt] -= 1
                if indeg[nxt] == 0:
                    q.append(nxt)

        return order if len(order) == numCourses else []