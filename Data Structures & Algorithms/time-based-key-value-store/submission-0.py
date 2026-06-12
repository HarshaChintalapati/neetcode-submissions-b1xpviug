class TimeMap:

    def __init__(self):
        self.store={}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key]=[]
        self.store[key].append([timestamp,value])
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        res=""
        l=0
        history=self.store[key]
        r=len(history)-1
        while(l<=r):
            mid=(l+r)//2
            if history[mid][0] == timestamp:
                return history[mid][1]
            elif history[mid][0] < timestamp:
                res = history[mid][1]
                l = mid + 1         
            else:
                r = mid - 1        
                
        return res
        
