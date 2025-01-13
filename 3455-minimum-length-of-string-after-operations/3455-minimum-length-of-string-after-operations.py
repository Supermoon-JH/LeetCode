class Solution:
    def minimumLength(self, s: str) -> int:
        # i = 1  
        # while i < len(s) - 1:  
        #     if s[i] in s[:i] and s[i] in s[i + 1:]:
        #         s = s[:i].replace(s[i], '', 1) + s[i] + s[i + 1:].replace(s[i], '', 1)
        #     else:
        #         i += 1  

        # return len(s)
        # Time Limit Exceeded
        
        new = Counter(s)

        count = 0
        for i in new.values():
            if i % 2 == 0:
                count += i - 2
            else:
                count += i - 1
        
        return len(s) - count