class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        numbers = {}
        counter = 0

        for num in nums:
            if num in numbers: 
                counter += numbers[num]
            numbers[num] = numbers.get(num, 0) + 1
        
        return counter 