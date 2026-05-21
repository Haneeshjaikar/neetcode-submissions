class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        sol = []
        for i in range(len(nums)):
            target = -(nums[i])
            j, k = i + 1, len(nums) - 1
            while j < k:
                curr = []
                if nums[j] + nums[k] == target:
                    curr.extend([nums[i], nums[j], nums[k]])
                    if curr not in sol:
                        sol.append(curr)
                    j+=1
                    k-=1
                    continue
                elif nums[j] + nums[k] > target:
                    k-=1
                    continue
                elif nums[j] + nums[k] < target:
                    j+=1
                    continue
        return sol
        