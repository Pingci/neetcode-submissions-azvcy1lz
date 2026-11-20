class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        res = 0
        for i in nums:
            cnt = 0
            if i - 1 not in numSet:
                while i in numSet:
                    i += 1
                    cnt += 1
                res = max(res, cnt)

        return res
