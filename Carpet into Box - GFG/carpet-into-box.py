#User function Template for python3


class Solution:
    def carpetBox(self, A,B,C,D):
        ans=0
        A,B=min(A,B),max(A,B)
        C,D=min(C,D),max(C,D)
        while(A>C or B>D):
            if(B>D):
                B//=2
                ans+=1
            elif(A>C):
                A//=2
                ans+=1
            A,B=min(A,B),max(A,B)
        return ans



#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():
        T=int(input())
        while(T>0):
            A,B,C,D = map(int, input().split())
            
            obj = Solution()
            print(obj.carpetBox(A,B,C,D))
            
            T-=1


if __name__ == "__main__":
    main()


# } Driver Code Ends