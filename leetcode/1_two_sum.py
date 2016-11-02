# 1. Two Sum
# Given an array of integers, return indices of the two numbers such that
# they add up to a specific target.

# You may assume that each input would have exactly one solution.

# Example:
# Given nums = [2, 7, 11, 15], target = 9,

# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].
# UPDATE(2016/2/13):
# The return format had been changed to zero-based indices. Please read
# the above updated description carefully.


class Solution(object):

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        array_length = len(nums)
        for first_index in xrange(array_length):
            for second_index in xrange(first_index+1, array_length):
                if nums[first_index] + nums[second_index] == target:
                    return [first_index, second_index]

        return []

# 16 / 16 test cases passed.
# Status: Accepted
# Runtime: 5042 ms


class Solution(object):

    def find(self, num, nums):
        indexes = []
        for index in xrange(len(nums)):
            if num == nums[index]:
                indexes.append(index)
        return indexes

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        import copy
        first_index = 0
        second_index = len(nums)-1
        nums_sorted = copy.copy(nums)
        nums_sorted.sort()
        while(first_index < second_index):
            if nums_sorted[first_index] + nums_sorted[second_index] < target:
                first_index += 1
            elif nums_sorted[first_index] + nums_sorted[second_index] > target:
                second_index -= 1
            else:
                return [min(self.find(nums_sorted[first_index], nums)), max(self.find(nums_sorted[second_index], nums))]
        return []

# 16 / 16 test cases passed.
# Status: Accepted
# Runtime: 42 ms
