from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if s == t:
            return True
        sset = set(s)
        tset = set(t)
        if len(s) != len(t) or sset != tset:
            return False
        s_freq_map_fast = Counter(s)
        t_freq_map_fast = Counter(t)
        if s_freq_map_fast != t_freq_map_fast:
            return False
        else:
            return True
        