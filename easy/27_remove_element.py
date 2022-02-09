import time
from typing import List
start_time = time.time()

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        pointer = 0
        for i in range(len(nums)):
            if nums[i] == val:
                nums[pointer] = nums[i]
                pointer += 1
        return pointer

# nums = [0,1,2,2,3,0,4,2]
# val = 2
nums = [3,2,2,3]
val = 3
solution = Solution()
print(solution.removeElement(nums, val))
print("--- %s seconds ---" % (time.time() - start_time))