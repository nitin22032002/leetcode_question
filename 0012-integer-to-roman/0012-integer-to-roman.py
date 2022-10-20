class Solution:
    def intToRoman(self, num: int) -> str:
        d=[[[1,"I"],[5,"V"],[10,"X"]],[[10,"X"],[50,"L"],[100,"C"]],[[100,"C"],[500,"D"],[1000,"M"]],[[1000,"M"]]]
        ans=[]
        c=0
        while(num!=0):
            r=num%10
            b=d[c]
            if(r==5):
                ans.append(b[1][1])
            elif(r<5):
                if(r==4):
                    ans.append(b[0][1]+b[1][1])
                else:
                    ans.append(b[0][1]*(r))
            else:
                if(r==9):
                    ans.append(b[0][1]+b[2][1])
                else:
                    ans.append(b[1][1]+(b[0][1]*(r-5)))
            c+=1
            num//=10
        ans.reverse()
        return "".join(ans)