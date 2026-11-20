class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mydic = {}

        for i in nums:
            mydic[i] = mydic.get(i, 0) + 1

        sorted_num = sorted(mydic, key=lambda x: mydic[x], reverse=True)

        return sorted_num[:k]