import time
start_time = time.time()

class Solution:
    def longestCommonPrefix(self, strs):
        shortestString = min(strs, key=len)
        while shortestString:
            isPrefix = True
            for i in range(len(strs)):
                if shortestString not in strs[i][:len(shortestString)]:
                    isPrefix = False
                    break
            if isPrefix:
                return shortestString
            shortestString = shortestString[:-1]
        return ""

strs = ["dog","racecar","car"]
solution = Solution()
print(solution.longestCommonPrefix(strs))
print("--- %s seconds ---" % (time.time() - start_time))