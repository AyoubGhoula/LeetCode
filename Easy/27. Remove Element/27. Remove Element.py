class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        while val in nums:
            nums.pop(nums.index(val))