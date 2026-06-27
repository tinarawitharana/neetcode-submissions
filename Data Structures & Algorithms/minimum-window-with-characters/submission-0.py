class Solution:
    def minWindow(self, s: str, t: str) -> str:

        count_t ={}
        count_window = {}

        
        have = 0

        for c in t:
            count_t[c] = count_t.get(c, 0) + 1

        need = len(count_t)
        left = 0
        result = ""

        for right in range(len(s)):
            count_window[s[right]] = count_window.get(s[right], 0) + 1

            if s[right] in count_t and count_window[s[right]] == count_t[s[right]]:
                have += 1
            
            while have == need:

                if result == "" or (right-left+1) < len(result):
                    result = s[left:right+1]

                count_window[s[left]] -= 1
                if count_window[s[left]] == 0:
                    del count_window[s[left]]

                if s[left] in count_t and count_window.get(s[left], 0) < count_t[s[left]]:
                    have -=1

                left +=1

        return result 
            
        