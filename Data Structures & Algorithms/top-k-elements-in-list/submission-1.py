class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ctr = Counter(nums)
        sol = []
        top_k = ctr.most_common(k)
        for values in top_k:
            sol.append(values[0])
        return sol