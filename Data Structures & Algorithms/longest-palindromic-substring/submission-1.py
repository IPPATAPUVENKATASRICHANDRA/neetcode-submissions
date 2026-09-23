class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        # dp=[[0]*len(s) for _ in range(len(s))]

        # for i in range(len(s)):
        #     for j in range(len(s)):
        #         if i!=j and s[i]==s[j]:
        #             dp[i][j]=1
        
        # ans = s[0]

        # for i in range(len(dp)):
        #     for j in range(len(dp[i])):

        #         if dp[i][j] == 1:

        #             word = s[i:j + 1]

        #             if word == word[::-1]:

        #                 if len(word) > len(ans):
        #                     ans = word

        # return ans

        n = len(s)
        dp = [[0] * n for _ in range(n)]

        ans = s[0]

        for i in range(n):
            for j in range(i + 1, n):

                if s[i] == s[j]:
                    dp[i][j] = 1

                    word = s[i:j + 1]

                    if len(word) > len(ans) and word == word[::-1]:
                        ans = word

        return ans