# Exercise 1 (To do in preparation for the Seminar):
    # You have given a sorted list of numbers with no duplicates, and you need to find the pairs of
    # numbers in that list whose sum is equal to the given target value.
    # Numbers can be either positive, negative, or both.
        # a) Test Case 1:
        # Input: [-1, 1, 2, 4, 8], target = 7
        # Output: [(-1, 8)]
        # b) Test Case 2:
        # Input: [2, 4, 5, 7], target = 9
        # Output: [(2,7), (5, 4)]
        # c) Test Case 3:
        # Input: [2, 4, 5, 7], target = 8
        # Output: []
    # Write an algorithm to find all such pairs given a list and a target. Note there are two approaches
    # to the problem, one called brute force where we try all possible combination of pairs and keep
    # the correct one (computationally expensive), one cleverer that is far more efficient.

# Brute Force approach

def find_pairs_bf(nums:list[int], target) -> list[int]:
    res = []
    for index, n in enumerate(nums):
        if index != len(nums) - 1:
            for i in nums[(index + 1):len(nums)]:
                if n + i == target:
                    res.append((n, i))
    return res

# Two Pointers approach
# Can be applied as the input list is given to be sorted
# More efficient

def find_pairs_tp(nums:list[int], target) -> list[int]:
    left = 0
    right = len(nums) - 1
    res = []
    while left < right:
        currentSum = nums[left] + nums[right]
        if currentSum == target:
            res.append((nums[left], nums[right]))
            left += 1
            right -= 1
        elif currentSum < target:
            left += 1
        elif currentSum > target:
            right -= 1
    return res