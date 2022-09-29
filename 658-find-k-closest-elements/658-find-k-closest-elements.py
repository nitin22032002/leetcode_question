class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        j=self.upperBound(arr,x)
        i=self.lowerBound(arr,x)
        # print(i,j)
        ans=[]
        while(k>0):
            if(i>=0 and j<len(arr)):
                d1=x-arr[i]
                d2=arr[j]-x
                if(d1<=d2):
                    ans.append(arr[i])
                    i-=1
                else:
                    ans.append(arr[j])
                    j+=1
            elif(i>=0):
                ans.append(arr[i])
                i-=1
            else:
                ans.append(arr[j])
                j+=1
            k-=1
        ans.sort()
        return ans
    def upperBound(self,arr,target):
        start=0
        end=len(arr)-1
        while(start<end-1):
            mid=(start+end)//2
            if(arr[mid]<=target):
                start=mid
            else:
                end=mid
        if(arr[start]>target):
            return start
        elif(arr[end]>target):
            return end
        return len(arr)
    def lowerBound(self,arr,target):
        start=0
        end=len(arr)-1
        while(start<end-1):
            mid=(start+end)//2
            if(arr[mid]<=target):
                start=mid
            else:
                end=mid
        if(arr[end]<=target):
            return end
        elif(arr[start]<=target):
            return start
        return -1
        