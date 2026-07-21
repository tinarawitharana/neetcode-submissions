class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(t) != len(s):
            return False

        s_map = dict()
        t_map = dict()

        for char in s:
            s_map[char] = s_map.get(char, 0) + 1

        for char in t:
            t_map[char] = t_map.get(char, 0) + 1


        for key in s_map:
            if s_map[key] != t_map.get(key, 0):
                return False

        return True
        
        