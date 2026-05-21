class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_con = min(len(nums), 1)
        i = 0
        nums = sorted(nums)
        curr_con = 1
        while i < len(nums) - 1:
            val = nums[i]
            nums.pop(0)
            if nums[i] == val:
                continue
            elif nums[i] != val + 1:
                curr_con = 1
                continue
            curr_con+=1
            max_con = max(curr_con, max_con)
            continue
        return max_con
