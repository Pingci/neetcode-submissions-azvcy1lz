class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        res = []
        if len(nums) == 0:
            return []
        
        for i in range(len(nums)):
            tmp_list = nums.copy()
            tmp_list.pop(i)
            tmp_res = 1
            for n in tmp_list:
                tmp_res *= n
            res.append(tmp_res)

        return res        