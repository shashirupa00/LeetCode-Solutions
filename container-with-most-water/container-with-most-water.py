class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        i, j = 0, len(height)-1
        res = float("-inf")
        
        while i < j:
            
            res = max(res, min(height[i], height[j]) * (j - i))
            
            if height[i] > height[j]:
                j -= 1
            
            else:
                i += 1
        
        return res
        