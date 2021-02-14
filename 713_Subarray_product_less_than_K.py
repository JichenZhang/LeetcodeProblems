""" Your are given an array of positive integers nums.

Count and print the number of (contiguous) subarrays where the product of all the elements in the subarray is less than k.

Example 1:

Input: nums = [10, 5, 2, 6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are: [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6].
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.

Note:
0 < nums.length <= 50000.
0 < nums[i] < 1000.
0 <= k < 10^6. 

https://leetcode-cn.com/problems/subarray-product-less-than-k/

"""
from typing import List
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        result = 0
        l = 0
        r = 0
        product = 1
        while r < len(nums):
            product *= nums[r]
            if product >= k:
                print('_',product, l, r)
                product = 1
                l += 1
                r = l
            else:
                print(l,r)
                result += 1
                r += 1
                
        # to make things faster?
        if product < k and l+1 < r: # add all remaining windows
            x = r-l-1
            print(x,'addition', (x**2 + x)>>1)
            result += (x**2 + x)>>1
            return result

        return result


print(Solution().numSubarrayProductLessThanK([6,8,6,6,10,8,10,3,7,7,4,9,3,1], 121))   