class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        
        allowedSet = set([char for char in allowed])
        res = 0

        for word in words:
            flag = True
            for char in word:
                if char not in allowedSet:
                    flag = False
                    break
            res += 1 if flag else 0
        
        return res