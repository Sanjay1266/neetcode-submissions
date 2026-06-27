class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seens = []
        seent = []
        for i in s:
            seens.append(i)
        for j in t:
            seent.append(j)
        seens.sort()
        seent.sort()
        return (seens == seent)