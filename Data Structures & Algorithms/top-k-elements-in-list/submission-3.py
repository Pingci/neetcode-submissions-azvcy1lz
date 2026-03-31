class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums = sorted(nums)
        my_dict = dict()
        current = nums[0]
        cnt = 0
        max_cnt = 0
        for n in nums:
            if (current == n):
                cnt += 1
            else:               
                if (my_dict.get(cnt) is None):
                    my_dict[cnt] = set()
                    my_dict[cnt].add(current)
                else:
                    my_dict[cnt].add(current)
                
                if max_cnt < cnt:
                    max_cnt = cnt
                current = n
                cnt = 1
        if max_cnt < cnt:
            max_cnt = cnt
        if my_dict.get(cnt) is None:
            my_dict[cnt] = set()
            my_dict[cnt].add(current)
        else:
            my_dict[cnt].add(current)
        print(max_cnt)
        tmp_length = len(my_dict[max_cnt])
        res = list(my_dict[max_cnt])
        while tmp_length < k:
            max_cnt -= 1
            if max_cnt < 0:
                break
            if my_dict.get(max_cnt) is None:
                continue
            else:
                tmp_length += len(my_dict[max_cnt])
                for i in my_dict[max_cnt]:
                    res.append(i)

        return res