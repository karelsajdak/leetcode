import time
start_time = time.time()

class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        isDouble = True
        single = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        double = {'CM': 900, 'CD': 400, 'XC': 90, 'XL': 40, 'IX': 9, 'IV': 4}
        while s:
            if s[0:2] in double:
                result += double[s[0:2]]
                s = s[2:]
            else:
                isDouble = False
            if len(s) > 0 and not isDouble:
                if s[0] in single:
                    result += single[s[0]]                
                    s = s[1:]
                    isDouble = True
        return result


s = "MCMXCVI"

solution = Solution()
print(solution.romanToInt(s))
print("--- %s seconds ---" % (time.time() - start_time))