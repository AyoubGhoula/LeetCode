class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer=[0]*len(temperatures)
        stack=[]
        for day,temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]]<temp:
                last_day=stack.pop()
                t[last_day]=day-last_day
            stack.append(day)
        return answer
                    
            