class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for string in strs:
            sorted_str = ''.join(sorted(string))
            if sorted_str not in groups:
                groups[sorted_str] = [string]
            else:
                groups[sorted_str].append(string)
        return list(groups.values())
