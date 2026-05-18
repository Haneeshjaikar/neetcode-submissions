class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index, value in enumerate(nums):
            for idx2, vl2 in enumerate(nums):
                if idx2 == index:
                    continue
                if value + vl2 == target:
                    return [index, idx2]
        