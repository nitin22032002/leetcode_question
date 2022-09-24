class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        maxS=3*pow(2,n-1)
        if(k>maxS):
            return ""
        else:
            ans=[]
            while(n!=0):
                t=pow(2,n-1)
                if(len(ans)==0):
                    if(k<=t):
                        ans.append("a")
                    elif(k<=(2*t)):
                        ans.append("b")
                        k-=t
                    else:
                        ans.append("c")
                        k-=(2*t)
                else:
                    if(k<=t):
                        if(ans[-1]=="a"):
                            ans.append("b")
                        else:
                            ans.append("a")
                    else:
                        if(ans[-1]=="a"):
                            ans.append("c")
                        elif(ans[-1]=="b"):
                            ans.append("c")
                        else:
                            ans.append("b")
                        k-=t
                n-=1
        return "".join(ans)
                        