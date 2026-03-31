from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()  # store indices, nums[dq] is decreasing
        res = []

        for r, x in enumerate(nums):
            # 1) maintain decreasing deque
            while dq and nums[dq[-1]] <= x:
                dq.pop()
            dq.append(r)

            # 2) remove indices out of window (left bound = r-k+1)
            left = r - k + 1
            if dq[0] < left:
                dq.popleft()

            # 3) once we formed a window, record max
            if left >= 0:
                res.append(nums[dq[0]])

        return res