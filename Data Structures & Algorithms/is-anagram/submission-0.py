class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        counter_t ={}
        counter_s = {}

        for letter in s:
            if letter not in counter_s:
                counter_s[letter] = 1
            else:
                counter_s[letter] += 1 

        for letter in t:
            if letter not in counter_t:
                counter_t[letter] = 1
            else:
                counter_t[letter] += 1 

        return counter_s == counter_t
        
        


        
        