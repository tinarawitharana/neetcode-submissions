class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        count = {}
        left = 0
        max_length = 0

        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1

            most_freq = max(count.values())

            window = right - left + 1
            changes = window - most_freq

            if changes > k:
                count[s[left]] -= 1
                left +=1
            
            max_length = max(max_length, right - left+1)


        return max_length
        