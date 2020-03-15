class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        reversen = 0
        while (x!=0):
            mode = x % 10
            x = x/10
            reversen = reversen * 10 + mode

        if reversen >=2**31-1 or reversen <= -2**31:
            return 0
        return reversen