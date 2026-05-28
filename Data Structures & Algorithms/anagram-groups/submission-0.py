from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        for s in strs:
            sortS = ''.join(sorted(s))
            ans[sortS].append(s)
        return list(ans.values())