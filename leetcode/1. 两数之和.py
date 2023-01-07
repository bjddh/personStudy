from time_laps import time_laps
from time_laps import logger


class Solution:
    @time_laps
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        len_Nums = len(nums)
        find_list = []
        for index in range(len_Nums):
            for index2 in range(index + 1, len_Nums):
                if nums[index] + nums[index2] == target:
                    find_list.append(index)
                    find_list.append(index2)
                    return find_list


s1 = Solution()
nums = [1, 2, 6, 11, 15, 101, 23, 4, 5]
target = 9
findlist = s1.twoSum(nums, target)
print(findlist)
