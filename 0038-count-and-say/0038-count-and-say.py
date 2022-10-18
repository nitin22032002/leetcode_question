class Solution:
    def countAndSay(self, n: int) -> str:
        if(n==1):
            return "1"
        else:
            ans=self.countAndSay(n-1)
            # print(ans)
            arr=[]
            i=0
            while(i<len(ans)):
                j=i
                while(j<len(ans) and ans[i]==ans[j]):
                    j+=1
                arr.append(str(j-i))
                arr.append(ans[i])
                i=j
            return "".join(arr)