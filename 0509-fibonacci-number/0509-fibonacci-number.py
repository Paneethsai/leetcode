class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        f1=0
        f2=1
        
        for i in range(0,n):
            
            temp=f1
            f1=f2
            f2=temp+f2
            
        return f1