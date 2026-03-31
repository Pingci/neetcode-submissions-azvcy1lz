class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        num_set = set(nums)

        for i in num_set:
            nums.remove(i)

        return list(set(nums))[0]