class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique_len = len(set(nums))
        if unique_len != len(nums):
            return True
            
        else:
            return False