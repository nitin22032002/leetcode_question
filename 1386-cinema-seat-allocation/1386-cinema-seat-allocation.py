class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        d={}
        for item in reservedSeats:
            r,c=item
            if(r not in d):
                d[r]=0
            b=1<<(c)
            d[r]|=b
        left=n-len(d)
        ans=2*left
        # print(ans)
        for item in d:
            col=d[item]
            # print(col)
            group=[[2,5],[4,7],[6,9]]
            for val in group:
                status=True
                a=val[0]
                while(a<=val[1]):
                    b=1<<a
                    if(col&b!=0):
                        status=False
                        break
                    else:
                        col|=b
                    a+=1
                if(status):
                    # print(item,val)
                    ans+=1
                else:
                    b=val[0]
                    while(b<a):
                        c=1<<b
                        col^=c
                        b+=1
        return ans
                    