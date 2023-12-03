class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n = min(len(word1), len(word2))
        answer = ""

        for i in range(n):
            answer += word1[i]
            answer += word2[i]
        
        if len(word1) > n:
            answer += word1[n : ]
        elif len(word2) > n:
            answer += word2[n : ]
        return answer