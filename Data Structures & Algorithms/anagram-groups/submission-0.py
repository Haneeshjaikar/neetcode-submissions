class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        pairs = set()
        sol = []
        for idx, val in enumerate(strs):
            if idx in pairs:
                continue
            curr=[val]
            pairs.add(idx)
            for idx2, val2 in enumerate(strs[idx+1:], start=idx+1):
                if idx2 in pairs:
                    continue
                if len(val) != len(val2) or Counter(val) != Counter(val2):
                    continue
                curr.append(val2)
                pairs.add(idx2)
            sol.append(curr)

        return sol