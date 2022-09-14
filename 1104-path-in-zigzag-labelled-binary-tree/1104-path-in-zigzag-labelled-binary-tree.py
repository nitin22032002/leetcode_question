from math import log,ceil
class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        height=int(log(label)/log(2))+1
        total=pow(2,height)-1
        return self.get(height,total,-1,label)
    def get(self,height,total,p,target):
        if(p==0 or target==1):
            return [1]
        elif(p==-1):
            child=pow(2,height-1)
            r1=total-child+1
            r2=r1+child-1
            dire=(height%2)
            if(dire==0):
                diff=r2-target
                ch=(r1-1)+diff
                par=ch
            else:
                par=target-1
            # print(par)
            if(par%2==0):
                par=int((par-2)/2)
            else:
                par=int((par-1)/2)
            ans=self.get(height-1,total-child,par,target)    
            ans.append(target)
            return ans
        else:
            child=pow(2,height-1)
            r1=total-child+1
            r2=r1+child-1
            dire=(height%2)
            if(p%2==0):
                par=int((p-2)/2)
            else:
                par=int((p-1)/2)
            ans=self.get(height-1,total-child,par,target)
            if(dire==0):
                diff=p-(r1-1)
                ans.append(r2-diff)
            else:
                ans.append(p+1)
            # print(ans)
            # print(height,child,r1,r2,p)
            return ans
                