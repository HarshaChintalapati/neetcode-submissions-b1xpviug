class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        arr=[[] for i in range(len(nums)+1)]
        for n in nums:
            count[n]=1+count.get(n,0)
        for n,c in count.items():
            arr[c].append(n)
        res=[]
        for i in range(len(arr)-1,0,-1):
            for num in arr[i]:
                res.append(num)
                if len(res)==k:
                    return res
        