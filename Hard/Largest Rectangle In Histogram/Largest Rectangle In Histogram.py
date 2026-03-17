
from ast import List



class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n=len(heights)
        t=set()
        for i in range(n) :
            Min=i
            w=1
            for j in range(i+1,n):
                if heights[Min] > heights[j] :
                    t.add(heights[Min]*w)
                    Min=j
                w+=1
            t.add(heights[Min]*w)
        return max(t)


