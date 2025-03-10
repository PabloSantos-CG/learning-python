from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]: # type:ignore
        length = len(nums)

        for aux1 in range(length-1):
            for aux2 in range(-1,-length, -1):
                result = nums[aux1] + nums[aux2]
                if result == target:
                    return [aux1, aux2]

list_nums = [1,2,3]
target = 3
solution = Solution()
aux1, aux2 = solution.twoSum(list_nums, target)

print(f'{list_nums[aux1]} + {list_nums[aux2]} = {target}')