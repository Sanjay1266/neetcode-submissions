class Solution:
    def isValid(self, s: str) -> bool:
        arr = []
        mapping = {')': '(', '}': '{', ']': '['}
        for i in s:
            if i in mapping.values():
                arr.append(i)
            elif i in mapping:
                if not arr or arr.pop() != mapping[i]:
                    return False
        if arr == []:
            return True 
            
        else:
            return False