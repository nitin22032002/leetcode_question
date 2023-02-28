class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        arr=[-1 for _ in range(2*n-1)]
        status=self.get(arr,0,0,n)
        # print(status)
        return arr
    def get(self,arr,i,bit,n):
        # print(i,arr)
        if(i>=len(arr)):
            # print(arr)
            return True
        elif(arr[i]!=-1):
            return self.get(arr,i+1,bit,n)
        else:
            for j in range(n,0,-1):
                if((bit>>j)&1!=0 or (j!=1 and ((j+i)>=len(arr) or arr[j+i]!=-1))):continue
                arr[i]=j
                if(j!=1):
                    arr[i+j]=j
                status=self.get(arr,i+1,bit|(1<<j),n)
                if(status):return True
                arr[i]=-1
                if(j!=1):
                    arr[i+j]=-1
            return False