class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        answer=[0]*len(temperatures)
        stack=[]
        for day,temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]]<temp:
                last_day=stack.pop()
                answer[last_day]=day-last_day
            stack.append(day)
        return answer
                    
            