class Solution:
    def maximumSwap(self, num: int) -> int:
        a=[]
        while(num!=0):
            a.append(num%10)
            num//=10
        a.reverse()
        t=[[a[i],i] for i in range(len(a))]
        def key(val):
            return [1/(val[0]+1),val[1]]
        t.sort(key=key)
        # print(t,a)
        for i in range(len(a)):
            if(a[i]!=t[i][0]):
                k=i+1
                while(k<(len(a)) and t[k][0]==t[i][0]):
                    k+=1
                k-=1
                # print(k,i,a)
                a[i],a[t[k][1]]=a[t[k][1]],a[i]
                break                
        ans=0
        for i in range(len(a)):
            ans=(ans*10)+a[i]
        return ans
            
        
        