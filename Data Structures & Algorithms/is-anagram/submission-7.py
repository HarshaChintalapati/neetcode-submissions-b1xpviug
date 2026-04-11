class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s)!=len(t)):
            return False
        sum={}
        sum1={}
        for i in range(len(s)):
            sum[s[i]]=1 + sum.get(s[i],0)
            sum1[t[i]]=1+ sum1.get(t[i],0)
        for j in sum:
            if(sum[j]!=sum1.get(j,0)):
                return False
        return True


        
        