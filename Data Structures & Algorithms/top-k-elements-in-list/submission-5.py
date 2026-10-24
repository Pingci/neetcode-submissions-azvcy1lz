class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mydic = {}
        for i in range(len(nums)):
            mydic[nums[i]] = mydic.get(nums[i], 0) + 1

        sorted_nums = sorted(mydic, key=lambda x: mydic[x], reverse=True)

        return sorted_nums[:k]