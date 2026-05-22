class Solution:
    def getArea(self, l: int, r: int, nums: List[int]) -> int:
        return (r-l) * (min(nums[r], nums[l]))

    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        max_area = 0
        while l<r:
            curr = self.getArea(l, r, heights)
            if curr > max_area:
                max_area = curr
            if heights[l] > heights[r]:
                r-=1
            else:
                l+=1
        
        return max_area
            

