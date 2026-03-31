class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_dict = dict()

        for i in strs:
            tmp = ''.join(sorted(i))
            if my_dict.get(tmp) is None:
                my_dict[tmp] = [i]
            else:
                my_dict[tmp].append(i)

        return ([j for j in my_dict.values()])