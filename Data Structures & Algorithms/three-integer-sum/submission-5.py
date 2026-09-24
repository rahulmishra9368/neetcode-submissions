class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        print(nums)
        results = []
        if nums[0] > 0:
                return []
        for i in range(len(nums)):
            j = i+1 
            k = len(nums)-1
            while j < k:
                if nums[j] + nums[k] == -nums[i] :
                    res = sorted([nums[i],nums[j],nums[k]])
                    if res not in results:
                        results.append(res)
                if nums[j] + nums[k] <= -nums[i]:
                    j += 1
                else:
                    k -= 1
                



            # for j in range(len(nums)):
            #     if i == j:
            #         continue
            #     for k in range(len(nums)):
            #         if k == j or k == i:
            #             continue
            #         if nums[i] + nums[j] + nums[k] == 0:
            #             res = sorted([nums[i],nums[j],nums[k]])
            #             if res not in results:
            #                 results.append(res)
        return results

   