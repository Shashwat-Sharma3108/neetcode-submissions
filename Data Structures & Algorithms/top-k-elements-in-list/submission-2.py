class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        required_dict = defaultdict(int)
        for num in nums:
            required_dict[num]+=1
        return [x[0] for x in sorted(required_dict.items(), key=lambda x:x[-1], reverse=True)][:k]
        
            