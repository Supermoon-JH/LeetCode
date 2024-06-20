class Solution:
    def isPalindrome(self, x: int) -> bool:
        l = []
        l = list(str(x))
        l.reverse()
        
        if list(str(x)) == l:
            return True
        else:
            False
        
        
        