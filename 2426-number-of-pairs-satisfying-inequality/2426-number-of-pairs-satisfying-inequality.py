class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        arr=[]
        self.diff=diff
        for i in range(len(nums1)):
            arr.append(nums1[i]-nums2[i])
        # print(arr)
        ans=self.get(arr,0,len(arr)-1)
        return ans
    def get(self,arr,start,end):
        mid=(start+end)//2
        if(start==end):
            return 0
        a=0
        a+=self.get(arr,start,mid)
        a+=self.get(arr,mid+1,end)
        a+=self.merge(arr,start,mid,end)
        return a
    def merge(self,arr,start,mid,end):
        i=start
        # print(arr)
        j=mid+1
        l=[]
        ans=0
        while(i<=mid and j<=end):
            if(arr[i]<arr[j]):
                x=self.upper(arr,arr[i]-self.diff,j,end)
                # print(x,arr[i],arr[j],end)
                ans+=end-x+1
                l.append(arr[i])
                i+=1
            else:
                # if(arr[i]-arr[j]<=self.diff):
                x=self.lower(arr,self.diff+arr[j],i,mid)
                # print(x,arr[i],arr[j],i)
                ans+=(x-i+1)
                l.append(arr[j])
                j+=1
            
        while(i<=mid):
            l.append(arr[i])
            i+=1
        while(j<=end):
            l.append(arr[j])
            j+=1
        t=start
        # print((start,end,mid),ans)
        while(start<=end):
            arr[start]=l[start-t]
            start+=1
        return ans
    def lower(self,arr,target,start,end):
        t=start
        while(start<end-1):
            mid=(start+end)//2
            if(arr[mid]>target):
                end=mid
            else:
                start=mid
        if(arr[end]<=target):
            return end
        elif(arr[start]<=target):
            return start
        return t-1
    def upper(self,arr,target,start,end):
        t=end+1
        while(start<end-1):
            mid=(start+end)//2
            if(arr[mid]>=target):
                end=mid
            else:
                start=mid
        if(arr[start]>=target):
            return start
        elif(arr[end]>=target):
            return end
        return t
            