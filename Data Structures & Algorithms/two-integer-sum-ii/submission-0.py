class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # numbers non decreasing
        # return index i j such i < j and numbers[i] + numbers[j] = target
        # edge case: out of bounds for i + 1
        '''
        for i from 0 to length of numbers - 1
            for j from i + 1 to len of numbers
                if num[i] + nums[j] is target
                    return i,j
        '''
        for i in range(len(numbers) - 1): 
            for j in range(i + 1, len(numbers)):
                if numbers[i] + numbers[j] == target: 
                    return [i + 1,j + 1]

        return None
        