class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        i=0
        while((i*i)<=c):
            t=(c-(i*i))
            if(t<=(i*i)):
                ans=self.find(0,i,t)
            else:
                ans=self.find(i,c,t)
            if(ans):
                return True
            i+=1
        return False
    
    def find(self,start,end,target):
        while(start<end-1):
            mid=(start+end)//2
            qu=mid*mid
            if(qu==target):
                return True
            elif(qu<target):
                start=mid
            else:
                end=mid
        return ((start*start)==target or (end*end)==target)