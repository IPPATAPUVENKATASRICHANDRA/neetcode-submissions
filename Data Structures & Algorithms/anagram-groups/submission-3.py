import collections
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # valid = [0] * len(strs)
        # ans = []

        # for i in range(len(strs)):
        #     if valid[i] == 1:
        #         continue

        #     cnt = collections.Counter(strs[i])
        #     temp = [strs[i]]

        #     for j in range(i + 1, len(strs)):
        #         if valid[j] == 0 and cnt == collections.Counter(strs[j]):
        #             temp.append(strs[j])
        #             valid[j] = 1

        #     ans.append(temp)

        # return ans

        ans=defaultdict(list)

        for word in strs:
            keyss=tuple(sorted(word))
            ans[keyss].append(word)
        
        return list(ans.values())


