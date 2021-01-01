class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        val = str(x)
        if (val[:: -1] == val): 
            return True 
        else:
            return False 
        