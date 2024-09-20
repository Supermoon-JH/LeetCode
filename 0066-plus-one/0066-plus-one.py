class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = int(''.join(map(str, digits))) + 1

        answer = [int(i) for i in str(num)]

        return answer