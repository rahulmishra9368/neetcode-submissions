class Solution:
    def isPalindrome(self, s: str) -> bool:
        # s = s.split()
        s = [x.lower() for x in s if ('a' <= x.lower()<='z' ) or ('0' <= x<='9')]
        s = "".join(s)
        print(s)
        return s == s[::-1]