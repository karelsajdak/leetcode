import time
from typing import List
start_time = time.time()

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 1
        unique = 1
        while index < len(nums):
            if nums[index-1] != nums[index]:
                nums[unique] = nums[index]
                unique += 1
            index += 1
        return unique

nums = [0,0,1,1,1,2,2,3,3,4]
solution = Solution()
print(solution.removeDuplicates(nums))
print("--- %s seconds ---" % (time.time() - start_time))