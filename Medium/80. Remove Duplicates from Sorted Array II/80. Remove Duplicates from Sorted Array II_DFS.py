class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        for i in set(nums):
            while nums.count(i)>2:
                nums.pop(nums.index(i))