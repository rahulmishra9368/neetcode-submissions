class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if not nums:
            return 0
        elif n == 1:
            return nums[0]
        elif n == 2:
            return max(nums[0],nums[1])


        memo = [0] * n
        memo[0] = nums[0]
        memo[1] = max(nums[0],nums[1])

        for i in range(2,n):
            rob = nums[i] + memo[i-2]

            skip = memo[i-1]
            memo[i] = max(rob,skip)

        return memo[i]
        # def decision(i):
        #     if i < 0 :
        #         return 0
        #     if i in memo:
        #         return memo[i]

        #     rob = nums[i] + decision(i-2)

        #     skip = decision(i-1)

        #     memo[i] = max(rob,skip)
        #     return max(rob,skip)

        # return decision(n-1)

        