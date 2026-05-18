class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        sol = {}
        for i in nums:
            if i in sol:
                return True
            sol[i] = 1
        return False