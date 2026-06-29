class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_prod = [1]
        suffix_prod = [1]
        n = len(nums)
        for x in nums:
            prefix_prod.append(prefix_prod[-1]*x)
        
        for x in nums[::-1]:
            suffix_prod.append(suffix_prod[-1]*x)
        
        result = [prefix_prod[i-1] * suffix_prod[n-i] for i in range(1, n+1)]
        return result