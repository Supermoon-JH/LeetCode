class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]

        prev = self.getRow(rowIndex - 1)
        new = [1] * (rowIndex + 1)

        for i in range(1, rowIndex):
            new[i] = prev[i - 1] + prev[i]

        prev.append(new)

        return prev[-1]