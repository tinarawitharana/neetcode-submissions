class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        right_array = []
        left_array = []
        run1 = 1

        for i in range(len(nums)):
            left_array.append(run1)
            run1 = run1 * nums[i]


        run2 = 1
        for i in range(len(nums)-1, -1, -1):
            right_array.append(run2)
            run2 = run2 * nums[i]

        right_array = right_array[::-1]

        output = []

        for i in range(len(nums)):
            output.append(right_array[i] * left_array[i])
        return output 