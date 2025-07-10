from typing import List, Self

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counters = {}
        for myInt in nums:
            if myInt not in counters:
                counters[myInt] = nums.count(myInt)
        sorted_counters = dict(sorted(counters.items(), key=lambda item: item[1]))
        return list(sorted_counters.keys())[-k:]

    print(topKFrequent(Self, [5,1,1,1,2,2,7,7,7,7], 2))
            