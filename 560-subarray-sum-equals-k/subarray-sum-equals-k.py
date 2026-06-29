from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum_freq = defaultdict(int)
        running_sum = 0
        num_subarrays = 0

        # 1. If running_sum == k; res += 1
        # 2. If running_sum - k == already_seen; res += num_times_seen

        for i, x in enumerate(nums):
            running_sum += x
            key = running_sum - k


            if key == 0:
                num_subarrays += 1
            if key in sum_freq:
                num_subarrays += sum_freq[key]

            sum_freq[running_sum] += 1
        return num_subarrays

