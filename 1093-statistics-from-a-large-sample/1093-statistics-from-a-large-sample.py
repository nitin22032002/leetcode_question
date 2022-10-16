class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:
        total=sum(count)
        # print(total)
        minElement=-1
        maxElement=-1
        sumElement=0
        if(total%2==0):
            mid=total//2
        else:
            mid=(total+1)//2
        median=0
        x1=-1
        x2=-1
        mode=0
        c=0
        for i in range(len(count)):
            if(count[i]!=0):
                if(minElement==-1):
                    minElement=i
                maxElement=i
            sumElement+=(i*count[i])
            c+=count[i]
            # print(c,i)
            if(x1==-1 and c>=mid):
                x1=i
            if(x2==-1 and total%2==0 and c>=(mid+1)):
                x2=i
            if(count[i]>count[mode]):
                mode=i
        if(total%2!=0):
            median=x1
        else:
            median=(x1+x2)/2
        return minElement,maxElement,(sumElement/total),median,mode
            
        