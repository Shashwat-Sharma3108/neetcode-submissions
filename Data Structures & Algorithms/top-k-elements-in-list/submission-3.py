class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        required_dict = defaultdict(int)
        for num in nums:
            required_dict[num]+=1
        
        hq = []

        for num in required_dict.keys():
            heapq.heappush(hq, (required_dict[num], num))
            if len(hq) > k:
                heapq.heappop(hq)
        res = []
        for i in range(k):
            res.append(heapq.heappop(hq)[1])
        return res
            