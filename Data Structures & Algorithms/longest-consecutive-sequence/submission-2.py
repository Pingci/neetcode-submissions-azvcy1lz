class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0

        sorted_list = list(sorted(set(nums)))
        print(sorted_list)
        my_dict = dict()
        cnt = 0
        cnt_set = set()
        for i in range(len(sorted_list)):
            curr = sorted_list[i]
            if i + 1 < len(sorted_list):
                if sorted_list[i+1] == curr + 1:
                    cnt += 1
                else:
                    cnt += 1
                    cnt_set.add(cnt)
                    cnt = 0
            else:
                if sorted_list[i] - 1 == sorted_list[i - 1]:
                    cnt_set.add(cnt+1)
                else:
                    cnt_set.add(1)

        return max(cnt_set)

        