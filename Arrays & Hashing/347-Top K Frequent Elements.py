class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = collections.Counter(nums)
        freq = [[] for i in range(len(nums)+1)]
        for key, val in counts.items():
            freq[val].append(key)
        res = []
        for indx in range(len(freq)-1,-1,-1):
            for num in freq[indx]:
                res.append(num)
                if len(res) == k:
                    return res
