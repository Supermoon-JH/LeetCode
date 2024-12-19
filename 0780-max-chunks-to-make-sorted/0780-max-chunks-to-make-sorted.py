class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        chunks = 1

        if len(arr) == 1:
            return chunks

        prefix = arr[:] # 1 2 0 3
        suffix = arr[:] # 1 2 0 3
        for i in range(1, len(arr)):
            prefix[i] = max(prefix[i], prefix[i - 1]) # 1 2 2 3

        for i in range(len(arr) - 2, -1, -1):
            suffix[i] = min(suffix[i], suffix[i + 1]) # 0 0 0 3
        print(prefix, suffix)
        for i in range(1, len(arr)):
            if prefix[i - 1] < suffix[i]:
                chunks += 1

        return chunks