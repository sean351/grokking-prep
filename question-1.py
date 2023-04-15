# Given an array of sorted numbers and a target sum, find a pair in the array whose sum is equal to the given target.

# Write a function to return the indices of the two numbers (i.e. the pair) such that they add up to the given target.

# Input [1,2, 3, 4, 6] target = 6
# Output [1,3]

class Solution:
    def twoSum(nums, target):
        # Binary Search
        left, right = 0, len(nums) - 1
        while left < right: # while the right pointer does not cross the left pointer
            curr = nums[left] + nums[right]
            if curr == target:
                return [left, right]
            
            if target > curr:
                left += 1
            else: 
                right -= 1
        return [-1, -1]

# Time: O(n) where n is the number of elements in the given array
# Space: O(1) constant space

def main():
  print(Solution.twoSum([1, 2, 3, 4, 6], 6))
  print(Solution.twoSum([2, 5, 9, 11], 11))


main()