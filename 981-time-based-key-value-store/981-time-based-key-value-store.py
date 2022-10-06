from sortedcontainers import SortedList
class TimeMap:
    def __init__(self):
        self.d={}
        self.val={}
    def set(self, key: str, value: str, timestamp: int) -> None:
        if(key not in self.d):
            self.d[key]=SortedList()
        self.val[(key,timestamp)]=value
        obj=self.d[key]
        obj.add(timestamp)
    def get(self, key: str, timestamp: int) -> str:
        if(key not in self.d):
            return ""
        obj=self.d[key]
        i=obj.bisect_left(timestamp)
        # print(obj,i)
        if(i<len(obj) and obj[i]==timestamp):
            return self.val[(key,timestamp)]
        elif(i==0):
            return ""
        else:
            return self.val[(key,obj[i-1])]

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)