class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        index = 15
        while index >= 0:
            num = 3 ** index
            if(num <= n):
                n = n - num
            if(n == 0):
                return True
            index -= 1
        return False            