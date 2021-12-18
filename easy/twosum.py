import time
start_time = time.time()

class Solution:
    def twoSum(self, nums, target):
        hash = {}
        for i, n in enumerate(nums):
            diffence = target - n
            if diffence in hash:
                return [hash[diffence], i]
            hash[n] = i

nums = [8, 9, 10, 1, 2, 5]
target = 15

solution = Solution()
solution.twoSum(nums, target)
print("--- %s seconds ---" % (time.time() - start_time))