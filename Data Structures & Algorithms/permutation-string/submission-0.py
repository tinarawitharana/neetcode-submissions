class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        count_s1 = {}
        count_window = {}
        left = 0
        s_length = len(s1)

        for c in s1:
            count_s1[c] = count_s1.get(c, 0) + 1

        for right in range(len(s2)):
            count_window[s2[right]] = count_window.get(s2[right], 0) + 1

            if right >= s_length:
                count_window[s2[left]] -=1
                if count_window[s2[left]] == 0:
                    del count_window[s2[left]]
                left +=1

            if count_window == count_s1:
                return True
        
        return False
            