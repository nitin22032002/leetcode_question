#User function Template for python3

class Solution:
    def decodedString(self, s):
        return self.other(s)
    def other(self,s):
        tem=[]
        n=""
        for i in range(len(s)):
            # print(tem,n)
            if(s[i]=="["):
                tem.append(n)
                tem.append("[")
                n=""
            elif(s[i]=="]"):
                t=""
                while(tem[-1]!="["):
                    t=tem.pop()+t
                tem.pop()
                n=tem.pop()
                tem.append(int(n)*t)
                n=""
            elif(ord(s[i])>=ord("0") and ord(s[i])<=ord("9")):
                n+=s[i]
            else:
                tem.append(s[i])
        return "".join(tem)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()
        
        ob = Solution()
        print(ob.decodedString(s))
# } Driver Code Ends