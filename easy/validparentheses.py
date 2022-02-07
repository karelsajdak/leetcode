import time
start_time = time.time()

class Solution:
    def isValid(self, s: str) -> bool:
        validChars = ['()', '{}', '[]']
        while len(s) > 0:
            length = len(s)
            for i in validChars:
                s = s.replace(i, '')
            if length == len(s):
                return False
        return True

s = "(([]){})"
solution = Solution()
print(solution.isValid(s))
print("--- %s seconds ---" % (time.time() - start_time))