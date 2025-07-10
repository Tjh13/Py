from typing import List, Self

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        myDictionary = {}
        for word in strs:
            key = ''.join(sorted(word))
            if key not in myDictionary:
                myDictionary[key] = []
            myDictionary[key].append(word)
        return list(myDictionary.values())
    