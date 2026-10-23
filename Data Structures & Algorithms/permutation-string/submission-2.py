from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        key = defaultdict(int)
        curr = defaultdict(int)
        for i in range(len(s1)):
            key[s1[i]]+=1
            curr[s2[i]]+=1
        for right in range(len(s1),len(s2)):
            if key == curr:
                return True
            out = s2[right - len(s1)]
            curr[out]-=1
            if curr[out] == 0:
                del curr[out]
            curr[s2[right]]+=1

        return key == curr

