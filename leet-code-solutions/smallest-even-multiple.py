class Solution:
    def gcd(self, x, y: int, int) -> int:
        if(x % y == 0):
            return 1
        return gcd(y, x % y)
    
    def smallestEvenMultiple(self, n: int) -> int:
        return (2 * n) // gcd(2, n)