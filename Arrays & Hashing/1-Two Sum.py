class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = dict()
        for indx, x in enumerate(nums):
            y = target - x
            if y in d:
                return [indx, d[y]]
            else:
                d[x] = indx
