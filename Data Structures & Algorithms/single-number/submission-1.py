class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count={}
        for i,n in enumerate(nums):
            count[n]=1+count.get(n,0)
        for k,v in count.items():
            if v==1:
                return k

        