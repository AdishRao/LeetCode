# https://leetcode.com/problems/get-the-maximum-score/
class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        sum1 = sum2 = total = i = j = 0
        len1 = len(nums1)
        len2 = len(nums2)
        while ((i < len1) and (j < len2)):
            while ((i < len1) and (nums1[i] < nums2[j])):
                sum1 += nums1[i]
                i += 1
            while ((i < len1) and (j < len2) and (nums2[j] < nums1[i])):
                sum2 += nums2[j]
                j += 1
            if ((i < len1) and (j < len2) and (nums1[i] == nums2[j])):
                total += max(sum1, sum2) + nums1[i]
                i += 1
                j += 1
                sum1 = sum2 = 0
        while (i < len1):
            sum1 += nums1[i]
            i += 1
        while (j < len2):
            sum2 += nums2[j]
            j += 1
        total += max(sum1, sum2)
        return (total % (10**9+7))