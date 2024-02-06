class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        t={}
        for i in strs:
            ch = ''.join(sorted(i))
            if ch not in t:
                t[ch] = []
            t[ch].append(i)
        return list(t.values())
            