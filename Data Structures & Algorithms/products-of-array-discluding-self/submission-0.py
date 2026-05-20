class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        sol = []
        zero_index = -1
        product = 1
        length = 0
        for idx,val in enumerate(nums):
            length+=1
            if val == 0:
                if zero_index != -1:
                    return [0 for i in nums]
                zero_index = idx
                continue
            product = product * val
        if zero_index != -1:
            sol = [0] * length
            sol[zero_index] = product
            return sol
        for i in nums:
            sol.append(int(product/i))
        return sol
        