class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        answer = 0
        for i in columnTitle:
            answer = answer * 26 + ord(i) - 64

        return answer