class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        # answer = [0] * len(queries)
        # vowel = ['a', 'e', 'i', 'o', 'u']

        # for i in range(len(queries)):   # i = [0, 2]   
        #     count = 0
        #     for j in range(queries[i][0], queries[i][-1] + 1):
        #         if words[j][0] in vowel and words[j][-1] in vowel:
        #             count += 1
        #     answer[i] = count 

        # return answer

        prefix = [0] * (len(words) + 1)
        vowel = ['a', 'e', 'i', 'o', 'u']

        for i in range(1, len(words) + 1):
            if words[i - 1][0] in vowel and words[i - 1][-1] in vowel:
                prefix[i] += prefix[i - 1] + 1
            else:
                prefix[i] += prefix[i - 1]

        answer = []
        for l, r in queries:
            answer.append(prefix[r + 1] - prefix[l])

        return answer