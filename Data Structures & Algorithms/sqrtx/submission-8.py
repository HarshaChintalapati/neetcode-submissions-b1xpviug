class Solution:
    def mySqrt(self, x: int) -> int:
        if(x==0 or x==1):
            return x
        n=0
        for i in range(2,x):
            if(i*i>x):
                return i-1
        return -1
           

        
        