# Given an array of sorted numbers and a target sum, find a pair in the array whose sum is equal to the given target.

# Write a function to return the indices of the two numbers (i.e. the pair) such that they add up to the given target.

# Input [1,2, 3, 4, 6] target = 6
# Output [1,3]

class Solution:
    def twoSum(nums, target):
        prevMap = {} # value : index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i

# Time: O(n) 
# Space: worst O(n)
def main():
  print(Solution.twoSum([1, 2, 3, 4, 6], 6))
  print(Solution.twoSum([2, 5, 9, 11], 11))


main()