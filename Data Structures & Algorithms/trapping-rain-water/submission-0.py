class Solution:
    def trap(self, height: List[int]) -> int:

        prefix_left = [0] * len(height)
        running_max = 0 

        for i in range(len(height)):
            prefix_left[i] = running_max
            running_max = max(running_max, height[i])

        prefix_right = [0] * len(height) 
        running_max = 0

        for i in range(len(height)-1, -1,-1):
            prefix_right[i] = running_max
            running_max = max(running_max, height[i])

        total = 0
        for i in range(len(height)):
            water = min(prefix_left[i], prefix_right[i]) - height[i]
            if water > 0:
                total += water
        
        return total



        
        