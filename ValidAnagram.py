from typing import Self

class ValidAnagram:
    def isAnagram(self, s: str, t:str) -> bool:
        sortedS = sorted(s)
        sortedT = sorted(t)
        if sortedS == sortedT:
            return True
        return False
    