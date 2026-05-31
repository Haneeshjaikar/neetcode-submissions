class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_l = 0
        for i, val in enumerate(s):
            chars = set()
            for j in range(i,len(s)):
                if s[j] in chars:
                    break
                chars.add(s[j])
            if len(chars) > max_l:
                max_l = len(chars)
        return max_l
