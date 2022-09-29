class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        j=self.upperBound(arr,x)
        i=self.lowerBound(arr,x)
        # print(i,j)
        a1=[]
        a2=[]
        while(k>0):
            if(i>=0 and j<len(arr)):
                d1=x-arr[i]
                d2=arr[j]-x
                if(d1<=d2):
                    a1.append(arr[i])
                    i-=1
                else:
                    a2.append(arr[j])
                    j+=1
            elif(i>=0):
                a1.append(arr[i])
                i-=1
            else:
                a2.append(arr[j])
                j+=1
            k-=1
        
        a1.reverse()
        return a1+a2
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
        