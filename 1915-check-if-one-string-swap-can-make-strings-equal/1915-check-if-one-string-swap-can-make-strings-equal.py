class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        
        s1_list = list(s1)
        s2_list = list(s2)

        for i in range(len(s1) - 1):
            for j in range(i + 1, len(s2)):
                s1_list[i], s1_list[j] = s1_list[j], s1_list[i]
                if s1_list == s2_list:
                    return True
                s1_list[i], s1_list[j] = s1_list[j], s1_list[i]
			
        return False