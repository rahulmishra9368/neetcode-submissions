class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def find_distict(i):
            if i <=1 :
                return 1
            if i in memo:
                return memo[i]

            distinct_steps = find_distict(i-1) + find_distict(i-2)
            memo[i] = distinct_steps

            return memo[i]     

        return find_distict(n)
            


        