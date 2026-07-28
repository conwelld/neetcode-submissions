class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum_dict = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in sum_dict:
                return [sum_dict[diff], i]
            sum_dict[n] = i
        return sums
            


        