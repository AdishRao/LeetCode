#https://leetcode.com/problems/first-bad-version/

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = 1
        h = n
        flag = None
        while(True):
            m = (l+h)//2
            flag = isBadVersion(m)
            if (flag and isBadVersion(m-1)==False):
                return m
            elif flag:
                h = m-1
            else:
                l = m+1