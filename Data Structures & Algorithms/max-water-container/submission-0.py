class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #[1,7,2,5,4,7,3,6]

        leftmax= 0
        rightmax= len(heights)-1
        water_storage = 0 
        while leftmax < rightmax:
            max_height = min(heights[leftmax],heights[rightmax])
            max_width = rightmax-leftmax
            if max_height*max_width > water_storage :
                water_storage = max_height*max_width
            if heights[leftmax] <= heights[rightmax] :
                leftmax += 1
            else:
                rightmax -= 1
        return water_storage



        


    
