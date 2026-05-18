class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sol = []
        while len(strs):
            val = strs[0]
            curr=[val]
            strs.pop(0)
            idx2 = 0
            while idx2 < len(strs):
                val2 = strs[idx2]
                if Counter(val) != Counter(val2):
                    idx2 = idx2 + 1
                    continue
                curr.append(val2)
                strs.pop(idx2)
            sol.append(curr)

        return sol