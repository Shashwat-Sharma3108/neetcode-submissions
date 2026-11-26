class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxCapacity = float('-inf')
        l=0
        r=len(heights)-1

        while l<r:
            currentCapacity = min(heights[l], heights[r]) * abs(r-l)
            maxCapacity = max(currentCapacity, maxCapacity)
            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1
        return maxCapacity 