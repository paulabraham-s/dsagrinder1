class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if k > n:
            return 0

        freq = {}
        window_sum = 0
        max_sum = 0

        for i in range(k):
            num = nums[i]
            freq[num] = freq.get(num, 0) + 1
            window_sum += num

        if len(freq) == k:
            max_sum = window_sum

        for right in range(k, n):
            left = right - k
            left_num = nums[left]
            right_num = nums[right]

            freq[left_num] -= 1
            if freq[left_num] == 0:
                del freq[left_num]

            freq[right_num] = freq.get(right_num, 0) + 1
            window_sum += right_num - left_num

            if len(freq) == k:
                max_sum = max(max_sum, window_sum)

        return max_sum