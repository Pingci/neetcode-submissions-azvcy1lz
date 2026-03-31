class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        print(sorted_nums)
        res = []
        for (i, a) in enumerate(sorted_nums):
            if i > 0 and a == sorted_nums[i - 1]:
                continue
            l, r = i + 1, len(sorted_nums) - 1

            while l < r:
                if a + sorted_nums[l] + sorted_nums[r] > 0:
                    r -= 1
                elif a + sorted_nums[l] + sorted_nums[r] < 0:
                    l += 1
                else:
                    res.append([a, sorted_nums[l], sorted_nums[r]])
                    l += 1
                    while sorted_nums[l] == sorted_nums[l - 1] and l < r:
                        l += 1
        
        return res
        