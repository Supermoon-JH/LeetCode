class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        answer = 0

        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i + len(needle)] == needle:
                return i

        return -1