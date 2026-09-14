"""


nums                            [0,1,0,2,1,0,1,3,2,1,2,1]
max_l_height                    [0,0,1,1,2,2,2,2,3,3,3,3]
max_r_height                    [3,3,3,3,3,3,3,2,2,2,1,0]
min(max_l_height, max_r_height) [0,0,1,1,2,2,2,2,2,2,1,0] to calc how much water was trapped we need a min height of left and right boundaries
water_trapped                   [0,0,1,0,1,2,1,0,0,1,0,0] min(max_l_height, max_r_height) - nums[current_index] == trapped water
"""
def trapping_water(nums):
    if not nums:
        return 0
    
    water_trapped = 0
    l = 0
    r = len(nums) - 1
    max_l_height, max_r_height = nums[l], nums[r]
    
    while l < r:
        if max_l_height < max_r_height:
            l += 1
            max_l_height = max(max_l_height, nums[l])
            water_trapped += max_l_height - nums[l]
        else:
            r -= 1
            max_r_height = max(max_r_height, nums[r])
            water_trapped += max_r_height - nums[r]

        


    return water_trapped
        
t1 = trapping_water([0,1,0,2,1,0,1,3,2,1,2,1])

print(t1)