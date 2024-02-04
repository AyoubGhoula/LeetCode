class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        nums_set=set()
        k=0 
        for i in nums:
            if i not in nums_set:
                nums_set.add(i)
                nums[k]=i
                k+=1

        return k