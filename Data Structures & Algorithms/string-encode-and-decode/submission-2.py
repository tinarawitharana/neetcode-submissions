class Solution:

    def encode(self, strs: List[str]) -> str:

        result = ""

        for s in strs:
            result += str(len(s)) + "#" + s

        return result

    def decode(self, s: str) -> List[str]:

        decode = []
        i =0

        while i < len(s):
            j = s.index("#", i)
            l = int(s[i:j])
            decode.append(s[j+1: j+1+l])
            i = j+ 1 + l

        return decode

