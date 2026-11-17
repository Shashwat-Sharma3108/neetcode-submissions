class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for counter,value in enumerate(nums):
            hash[value] = counter

        for counter, value in enumerate(nums):
            required_value = target - value
            if required_value in hash:
                if counter != hash[required_value]:
                    return [counter, hash[required_value]]
                 
