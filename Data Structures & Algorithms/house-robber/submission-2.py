class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        memo = {}
        def decision(i):
            if i < 0 :
                return 0
            if i in memo:
                return memo[i]

            rob = nums[i] + decision(i-2)

            skip = decision(i-1)

            memo[i] = max(rob,skip)
            return max(rob,skip)

        return decision(n-1)

        