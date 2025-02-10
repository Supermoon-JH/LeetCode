class Solution:
    def clearDigits(self, s: str) -> str:
        # s_list = list(s)
        # index = 0

        # while index < len(s_list):
        #     if s_list[index].isdigit():
        #         del s_list[index]
        #         if index > 0:
        #             del s_list[index - 1]
        #             index -= 1
        #     else:
        #         index += 1


        # return "".join(s_list)
        # brute force

        # s_list = []

        # for i in s:
        #     if i.isdigit() and s_list:
        #         s_list.pop()
        #     else:
        #         s_list.append(i)

        # return "".join(s_list)
        # stack

        answer_len = 0
        s = list(s)

        for i in range(len(s)):
            if s[i].isdigit():
                answer_len = max(answer_len - 1, 0)
            else:
                s[answer_len] = s[i]
                answer_len += 1

        s = s[:answer_len]

        return "".join(s)