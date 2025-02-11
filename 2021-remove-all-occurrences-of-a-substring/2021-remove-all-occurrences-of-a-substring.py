class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        # def delete_part(s):
        #     new = s.replace(part, "", 1)
        #     return new

        # answer = s
        # while True:
        #     if answer == delete_part(answer):
        #         break
        #     answer = delete_part(answer)
        #     print(answer)
            
        # return answer
        # my answer

        while part in s:
            s = s.replace(part, "", 1)
        return s