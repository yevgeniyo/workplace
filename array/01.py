# Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.
# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.


class Solution:
    def removeDuplicates(self, nums):
        cl = []
        for i in nums:
            if i not in cl:
                cl.append(i)
        return len(cl)


x = Solution()
print(x.removeDuplicates([1,1,1,4]))