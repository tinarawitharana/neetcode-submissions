class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        hashmap = {}

        for n in nums:
            if n in hashmap:
                hashmap[n] += 1
            else:
                hashmap[n] =1

        result = sorted(hashmap, key = lambda x: hashmap[x], reverse=True)
            
        return result[:k]

        
        