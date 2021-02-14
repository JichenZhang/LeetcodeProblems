from typing import List
class Solution:
    def massage(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        max_minutes_if_taking = [None for i in range(n)]
        max_minutes_if_taking[n-1] = nums[n-1]
        max_minutes_if_taking[n-2] = max(nums[n-1],nums[n-2])
        for i in range(n-3, -1, -1):
            max_minutes_if_taking[i] = max(
                nums[i] + max_minutes_if_taking[i+2],
                max_minutes_if_taking[i+1]
            )
        # print (max_minutes_if_taking)
        return max(
            max_minutes_if_taking[0],
            max_minutes_if_taking[1]
        )
print(Solution().massage([1,2,3,1]))