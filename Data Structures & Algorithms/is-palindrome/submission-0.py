import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        t=s.lower()
        cleaned_s= re.sub(r'[^a-zA-Z0-9]','',t)

        if cleaned_s==cleaned_s[::-1]:
            return True
        else:
            return False