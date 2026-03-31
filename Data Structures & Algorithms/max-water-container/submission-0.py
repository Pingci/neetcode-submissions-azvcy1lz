class Solution:
    def maxArea(self, heights: List[int]) -> int:

        maxArea = 0

        l, r = 0, len(heights) - 1

        while l < r:
            tmpArea = (r - l) * min(heights[l], heights[r])
            if tmpArea > maxArea:
                maxArea = tmpArea
            
            if heights[l] < heights[r]:
                l += 1
            elif heights[l] > heights[r]:
                r -= 1
            else:
                tmpArea = (r - l) * min(heights[l], heights[r])
                if tmpArea > maxArea:
                    maxArea = tmpArea
                else:
                    l += 1
        return maxArea
        