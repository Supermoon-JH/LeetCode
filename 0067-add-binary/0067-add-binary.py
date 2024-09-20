class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a_decimal = int(a, 2)
        b_decimal = int(b, 2)

        answer = bin(a_decimal + b_decimal)[2:]

        return answer