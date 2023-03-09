class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        res = 0
        for n in seen:
            if n - 1 not in seen:
                seq = n
                ln = 0
                while seq in seen:
                    seq += 1
                    ln += 1
                res = max(res, ln)
        return res

