class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(filter(str.isalnum, s)).lower()
        
        if s == " " or s == '':
            return True
        elif len(s) == 1:
            return True

        queue = []
        for i in range(len(s) // 2):
            queue.append(s[i])
        
        for i in range(len(s) - 1, -1, -1):
            if not queue:
                return True
            if s[i] != queue.pop(0):
                return False