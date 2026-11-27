class Solution:
    def trap(self, height: List[int]) -> int:
        current_capacity = 0
        prefixMax = []
        suffixMax = [0]*len(height)
        for i in range(len(height)-1):
            if i == 0:
                prefixMax.append(height[i])
            else:
                prefixMax.append(max(height[i], prefixMax[i-1]))
        for i in range(len(height)-1, -1, -1):
            if i == len(height)-1:
                suffixMax[i] = height[i]
            else:
                suffixMax[i] = max(height[i], suffixMax[i+1])
        for i in range(len(height)-1):
            current_capacity += min(prefixMax[i], suffixMax[i]) - height[i]
        return current_capacity