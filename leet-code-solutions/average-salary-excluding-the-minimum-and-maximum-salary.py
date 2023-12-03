class Solution:
    def average(self, salary: List[int]) -> float:
        maximum = max(salary[0], salary[1])
        minimum = min(salary[0], salary[1])

        answer = 0.0
        for sal in salary[2:]:
            if sal > maximum:
                answer += maximum
                maximum = sal
            elif sal < minimum:
                answer += minimum
                minimum = sal
            else:
                answer += sal
            
        return answer / (len(salary) - 2)