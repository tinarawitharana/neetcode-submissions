class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        new_set = set()

        for n in nums:
            if n in new_set:
                return True

            new_set.add(n)

        return False