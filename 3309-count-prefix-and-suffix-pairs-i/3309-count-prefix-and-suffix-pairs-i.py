class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        answer = 0

        for i in range(len(words) - 1):
            for j in range(i + 1, len(words)):
                if self.check(words[i], words[j]):
                    answer += 1

        return answer

    def check(self, a, b):
        if len(a) <= len(b) and b[:len(a)] == a and b[-len(a):] == a:
            return True

        return False        