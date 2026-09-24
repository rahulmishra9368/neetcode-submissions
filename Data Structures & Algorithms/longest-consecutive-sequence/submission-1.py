class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
     
        if not nums:
            return 0
        longest = 1
        temp = 1
        next = nums[0]+1
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                    continue

            if nums[i] == next:
                next= nums[i] + 1
                
                temp += 1
                if temp >= longest:
                    longest = temp
                
            else:
                next = nums[i] + 1
                temp = 1

        return longest
            