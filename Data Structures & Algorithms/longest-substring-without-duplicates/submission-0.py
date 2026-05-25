class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        stor = set()

        l = 0
        max_len = 0

        for r in range(len(s)):

            while s[r] in stor:
                stor.remove(s[l])
                l += 1

            stor.add(s[r])

            max_len = max(max_len, r - l + 1)

        return max_len