class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        running_sum = 0
        max_len = 0
        first_sum_occurence = {}

        for i, x in enumerate(nums):
            running_sum += 1 if x==1 else -1
            if running_sum == 0:
                max_len = i+1
            elif running_sum in first_sum_occurence:
                subarray_len = i - first_sum_occurence[running_sum] 
                max_len = subarray_len if subarray_len > max_len else max_len
            else:
                first_sum_occurence[running_sum] = i
        return max_len