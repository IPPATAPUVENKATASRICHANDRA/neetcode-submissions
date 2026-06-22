class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        
        par = []
        res = []

        def dfs(i):
            if len(par) == 4:
                if i == len(s):
                    res.append(".".join(par))
                return

            for j in range(i, len(s)):
                part = s[i:j+1]

                # valid IP segment
                if len(part) > 1 and part[0] == '0':
                    break
                if int(part) > 255:
                    break

                par.append(part)
                dfs(j + 1)
                par.pop()

        dfs(0)

        return res