class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        answer = []
        
        for i in words:
            for j in words:
                if i != j and i in j:
                    answer.append(i)

        return list(set(answer))