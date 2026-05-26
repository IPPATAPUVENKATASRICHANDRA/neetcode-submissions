from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if len(s) < len(t):
            return ""

        t_counter = Counter(t)

        window_size = len(t)
        ans = ""

        while window_size <= len(s):

            l = 0

            while l + window_size <= len(s):

                s_window = s[l:l + window_size]
                s_counter = Counter(s_window)

                valid = True

                for ch in t_counter:
                    if s_counter[ch] < t_counter[ch]:
                        valid = False
                        break

                if valid:
                    return s_window   # first valid is minimum

                l += 1

            window_size += 1

        return ans