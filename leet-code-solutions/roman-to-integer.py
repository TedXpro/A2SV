class Solution:
    def romanToInt(self, s: str) -> int:
        romanNums = {}
        romanNums['I'] = 1
        romanNums['V'] = 5
        romanNums['X'] = 10
        romanNums['L'] = 50
        romanNums['C'] = 100
        romanNums['D'] = 500
        romanNums['M'] = 1000

        i = 0
        answer = 0
        while i < len(s):
            if i + 1 < len(s) and romanNums[s[i]] < romanNums[s[i + 1]]:
                answer += (romanNums[s[i + 1]] - romanNums[s[i]])
                i += 2
            else :
                answer += romanNums[s[i]]
                i += 1
                
        
        return answer