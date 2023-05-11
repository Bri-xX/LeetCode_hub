class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        map1 = {}
        for i in s1:
            if i not in map1:
                map1[i] = 1
            else:
                map1[i] += 1
        time = len(s2) - len(s1) + 1
        for i in range(time):
            map2 = {}
            sub = s2[i:i + len(s1)]
            for j in sub:
                if j not in map2:
                    map2[j] = 1
                else:
                    map2[j] += 1
            if map2 == map1:
                return True
        return False