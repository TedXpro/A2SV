class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        alphabets = {}
        for i in range(len(order)):
            alphabets[order[i]] = i

        
        for i in range(len(words) - 1):
            currentWord = words[i]
            nextWord = words[i + 1]

            size = min(len(currentWord), len(nextWord))
            status = False
            for j in range(size):
                if(alphabets[currentWord[j]] > alphabets[nextWord[j]]):
                    return False
                elif alphabets[currentWord[j]] < alphabets[nextWord[j]]: 
                    status = True
                    break
            
            if(len(currentWord) > size and not status):
                return False
            
        
        return True


# class Solution:
#     def isAlienSorted(self, words, order):
#         alphabets = {char: i for i, char in enumerate(order)}

#         for i in range(len(words) - 1):
#             current = words[i]
#             next_word = words[i + 1]

#             size = min(len(current), len(next_word))

#             status = False
#             for j in range(size):
#                 if alphabets[next_word[j]] < alphabets[current[j]]:
#                     return False
#                 if alphabets[next_word[j]] > alphabets[current[j]]:
#                     status = True
#                     break

#             if len(current) > len(next_word) and not status:
#                 return False

#         return True
