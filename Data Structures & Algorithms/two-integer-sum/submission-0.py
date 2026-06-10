class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hashmaps={}

        for i, num in enumerate(nums):
            integer = target - num
            if integer in hashmaps:
                return [hashmaps[integer], i]
            else:
                hashmaps[num] = i
        