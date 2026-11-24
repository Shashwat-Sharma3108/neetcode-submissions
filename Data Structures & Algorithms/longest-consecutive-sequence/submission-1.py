class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        currSet = set(nums)
        output = set()

        #NOTE: In python set behind the uses HashMap, which results in O(1) instead of O(n)

        for i in currSet:
            if i-1 not in currSet:
                length = 0
                while i + length in currSet:
                    length += 1
                longest = max(longest, length)
        return longest