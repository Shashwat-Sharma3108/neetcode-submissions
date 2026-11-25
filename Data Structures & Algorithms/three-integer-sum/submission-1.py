class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() #O(NLOGN)
        seen = set() 
        output = []
        
        for j in range(len(nums)):
            l=j+1
            r=len(nums)-1
            while l<r:
                temp = nums[j] + nums[l] + nums[r]
                if temp == 0 and (nums[j],nums[l],nums[r]) not in seen:
                    output.append([nums[j],nums[l],nums[r]])
                    seen.add(tuple([nums[j],nums[l],nums[r]]))
                    l+=1
                    r-=1
                elif temp > 0:
                    r-=1
                else:
                    l+=1
        return output
                
                