class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        required_dict = defaultdict(list)
        for word in strs:
            sortedS = ''.join(sorted(word))
            required_dict[sortedS].append(word)
        return list(required_dict.values())
