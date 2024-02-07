class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            index=target-nums[i]
            if index in nums and nums.index(index)!= i :
                return [nums.index(index),i]