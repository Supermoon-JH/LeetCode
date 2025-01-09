class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        answer = 0

        for i in words:
            if i.startswith(pref):
                answer += 1

        return answer