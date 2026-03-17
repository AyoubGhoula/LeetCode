
from typing import List



class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic={}
        for i in strs :
            str_sort=''.join(sorted(i))
            if str_sort in dic :
                dic[str_sort].append(i)
            else :
                dic[str_sort]=[i]
        result=[]
        for i in dic :
            result.append(dic[i])
        return result
        
