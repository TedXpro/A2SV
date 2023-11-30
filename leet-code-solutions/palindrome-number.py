class Solution:
    def isPalindrome(self, x: int) -> bool:
        if(x < 0):
            return False
        temp = x
        reverse = 0
        while temp > 0:
            rem = temp % 10
            reverse = reverse * 10 + rem
            temp //= 10

        return reverse == x