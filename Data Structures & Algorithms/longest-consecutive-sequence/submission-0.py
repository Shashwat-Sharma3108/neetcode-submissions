class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        currSet = set(nums)
        output = set()

        for i in currSet:
            if i-1 not in currSet:
                length = 0
                while i + length in currSet:
                    length += 1
                longest = max(longest, length)
        return longest