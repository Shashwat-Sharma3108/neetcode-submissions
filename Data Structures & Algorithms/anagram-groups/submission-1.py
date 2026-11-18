class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        required_dict = defaultdict(list)
        for word in strs:
            count = [0] * 26
            for s in word:
                count[ord(s) - ord('a')] += 1
            required_dict[tuple(count)].append(word)
        return list(required_dict.values())
