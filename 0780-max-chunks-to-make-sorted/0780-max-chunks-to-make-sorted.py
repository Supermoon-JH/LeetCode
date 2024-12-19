class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        chunks = 1

        if len(arr) == 1:
            return chunks

        prefix = arr[:] 
        suffix = arr[:] 
        for i in range(1, len(arr)):
            prefix[i] = max(prefix[i], prefix[i - 1])

        for i in range(len(arr) - 2, -1, -1):
            suffix[i] = min(suffix[i], suffix[i + 1])
        
        for i in range(1, len(arr)):
            if prefix[i - 1] < suffix[i]:
                chunks += 1

        return chunks