from typing import List, Self


class ContainsDuplicate:
    def containsDuplicate(self, nums: List[int]) -> bool:
        mySet = set(nums)
        if len(mySet) != len(nums):
            return True
        return False
    