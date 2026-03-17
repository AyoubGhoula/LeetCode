class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False 
        for i in set(list(s)):
            if list(s).count(i)!=list(t).count(i):
                return False
        return True