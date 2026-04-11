class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        sum={}
        for i in range (len(nums)):
            sum[nums[i]]=1+sum.get(nums[i],0)
        max_key=max(sum,key=sum.get)
        return max_key
    
        
        