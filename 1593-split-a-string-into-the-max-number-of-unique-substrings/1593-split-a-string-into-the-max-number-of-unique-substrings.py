class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        ans=self.get(s,0,0,{})
        return ans
    def get(self,s,i,bit,dp):
        if(i>=len(s)):
            # self.bits(bit)
            return 0
        elif((i,bit) in dp):
            return dp[(i,bit)]
        else:
            ans=0
            b=1<<i
            for j in range(i+1,len(s)+1):
                if(self.check(bit,s,i,j) or bit==0):
                    ans=max(ans,1+self.get(s,j,bit|b,dp))
            dp[(i,bit)]=ans
            return ans
    def check(self,bit,s,i,l):
        j=0
        start=i
        
        while(j<start):
            # print((i,j))
            if(i>=l or s[i]!=s[j]):
                j+=1
                while(j<start and (1<<j)&bit==0):
                    j+=1
                i=start
                continue
            else:
                i+=1
                j+=1
                b=1<<j
                if(bit&b!=0 or j==start):
                    if(i==l):
                        return False
                    i=start  
        return True
    def bits(self,n):
        arr=[]
        while(n!=0):
            arr.append(str(n%2))
            n//=2
        print("".join(arr))