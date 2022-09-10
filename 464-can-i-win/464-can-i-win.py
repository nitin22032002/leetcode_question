class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        s=((maxChoosableInteger)*(maxChoosableInteger+1))//2
        if(desiredTotal==0):
            return True
        elif(s<desiredTotal):
            return False
        d={}
        ans=self.get(maxChoosableInteger,desiredTotal,0,0,True,d)
        # print(d)
        return ans
    def get(self,n,total,curr,bit,state,d):
        if(curr>=total):
            return (not state)
        elif((curr,bit) in d):
            return d[(curr,bit)]
        else:
            for i in range(1,n+1):
                b=1<<(i)
                if(bit&b==0):
                    # print(b,i)
                    if(self.get(n,total,curr+i,bit|b,not state,d)==state):
                        d[(curr,bit)]= state
                        return state
            d[(curr,bit)]=(not state)
            return (not state)