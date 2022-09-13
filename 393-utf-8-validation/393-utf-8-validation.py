class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        i=0
        step=0
        while(i<len(data)):
            j=7
            while(j>=0 and (1<<j)&data[i]!=0):
                j-=1
            s=(7-j)
            # print(s,data[i])
            if(s>4 or (s==1 and step==0)):
                return False
            elif(step==0):
                if(s!=0):
                    step=s-1
            elif(s!=1):
                return False
            else:
                step-=1
            i+=1
        return step==0
    def binary(self,n):
        ans=[]
        while(n!=0):
            ans.append(str(n%2))
            n//=2
        print("".join(ans[::-1]))
            