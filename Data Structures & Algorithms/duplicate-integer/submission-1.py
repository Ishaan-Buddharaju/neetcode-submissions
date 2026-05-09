class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mySet = set()
        for number in nums:
            if number in mySet:
                return True
            else: 
                mySet.add(number)
        return False
        