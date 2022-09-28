class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        d={}
        for item in reservedSeats:
            r,c=item
            if(r not in d):
                d[r]=[False for _ in range(10)]
            d[r][c-1]=True
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
                    if(col[a-1]):
                        status=False
                        break
                    else:
                        col[a-1]=True
                    a+=1
                if(status):
                    # print(item,val)
                    ans+=1
                else:
                    b=val[0]
                    while(b<a):
                        col[b-1]=False
                        b+=1
        return ans
                    