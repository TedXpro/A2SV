class Solution:
    def interpret(self, command: str) -> str:
        answer = ""
        i = 0
        while i < len(command):
            if command[i] == 'G':
                answer += 'G'
            else :
                if command[i + 1] == ')':
                    answer += 'o'
                    i += 1
                else :
                    answer += "al"
                    i += 3
            i += 1
        
        return answer
