class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        elif len(nums)==1:
            return nums[0]
        elif len(nums)==2:
            return max(nums[0],nums[1])

        
        
        def max_amount(self,arr):
            n = len(arr)
            

            dp = [0]*n

            dp[0]= arr[0]
            dp[1]= max(dp[0],arr[1])
            


            for i in range(2,n):
                print(arr)
                print(i)
                rob = arr[i] + dp[i-2]
                skip= dp[i-1]
                dp[i] = max(rob,skip)

            return dp[-1]

        return max(max_amount(self,nums[1:len(nums)]),max_amount(self,nums[:len(nums)-1]))
       

        
            

        