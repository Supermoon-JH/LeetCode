class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        num = len(A)
        answer = []

        for i in range(num):
            freq = 0
            new = Counter(A[:i+1]) + Counter(B[:i+1])
            for value in new.values():
                if value == 2:
                    freq += 1
            answer.append(freq)

        return answer