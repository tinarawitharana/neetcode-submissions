class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        num_set = set(nums)
        longest=0

        for n in nums:
            if n - 1 not in num_set:
                current_num = n
                length = 1
                
                while current_num + 1 in num_set:
                    current_num +=1
                    length += 1
                
                
                longest = max(longest, length)
        return longest 