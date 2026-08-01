class Solution:
    def subarraySum(self, nums, k):
        prefixCount = {0: 1}
        prefix = 0
        answer = 0

        for num in nums:
            prefix += num

            if prefix - k in prefixCount:
                answer += prefixCount[prefix - k]

            prefixCount[prefix] = prefixCount.get(prefix, 0) + 1

        return answer