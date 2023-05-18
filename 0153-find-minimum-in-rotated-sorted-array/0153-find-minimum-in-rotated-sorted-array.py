class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l, r = 0, len(nums)-1

        while l<=r:
            mid = (l+r)//2
            res = min(res, nums[mid])

            if nums[mid] > nums[r]:
                res = min(res, nums[l])
                l = mid+1
            
            else:
                res = min(res,nums[r])
                r = mid-1

        return res

            
            






