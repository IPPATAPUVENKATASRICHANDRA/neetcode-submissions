class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        if t == s:
            return t

        # st_w = len(t)
        # target = sorted(t)

        # def helper(s1, b):
        #     a = sorted(s1)
        #     i = 0
        #     j = 0
        #     while i < len(a) and j < len(b):
        #         if a[i] == b[j]:
        #             i += 1
        #             j += 1
        #         elif a[i] < b[j]:
        #             i += 1
        #         else:
        #             return False
        #     return j == len(b)

        # st_w = len(t)
        # target = Counter(t)

        # def helper(s1, b):
        #     a = Counter(s1)
        #     for ch, cnt in b.items():
        #         if a[ch] < cnt:
        #             return False
        #     return True

        # while st_w <= len(s):
        #     for i in range(0, len(s) - st_w + 1):
        #         if helper(s[i : i + st_w], target):
        #             return s[i : i + st_w]

        #     st_w += 1

        # return ""
        countT, window = {}, {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        have, need = 0, len(countT)
        res, resLen = [-1, -1], float("infinity")
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in countT and window[c] == countT[c]:
                have += 1

            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1

                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l : r + 1] if resLen != float("infinity") else ""