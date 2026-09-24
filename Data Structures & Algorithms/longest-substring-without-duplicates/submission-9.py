class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        i = 0
        j = i+1
        max_count = 1
        while i < j and j < len(s):
            if s[j] in s[i:j]:
                i += s[i:j].index(s[j]) + 1
                j +=1
            else: 
                max_count = max(max_count,len(s[i:j+1]))
                j+=1
        return max_count