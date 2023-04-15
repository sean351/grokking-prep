class Solution:
    def removeDuplicates(nums):
        count = 1
        i = 0
        while(i < len(nums)):
            if nums[count - 1] != nums[i]:
                nums[count] = nums[i]
                count +=1
            i += 1
        return count
# Time: O(n) for n elements
# Space: O(1) constant space

# We use 1 pointer for iterating the array
# We use other pointer for inserting the next-non dup number