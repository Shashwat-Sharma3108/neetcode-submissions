class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() #O(NLOGN)
         
        output = set()
        
        for j in range(len(nums)):
            l=j+1
            r=len(nums)-1
            while l<r:
                temp = nums[j] + nums[l] + nums[r]
                if temp == 0 and j!=l!=r:
                    output.add((nums[j],nums[l],nums[r]))
                    l+=1
                    r-=1
                    while l<r and nums[l] == nums[l-1]:
                        l+=1
                elif temp > 0:
                    r-=1
                else:
                    l+=1
        return list(output)
                
                