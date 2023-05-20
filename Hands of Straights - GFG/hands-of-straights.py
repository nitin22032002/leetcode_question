#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

from collections import deque
class Solution:
    def isStraightHand(self, N, groupSize, hand):
        if(N%groupSize!=0):return False
        hand.sort()
        obj=deque()
        for item in hand:
            if(len(obj)==0 or obj[0][0]==item):
                obj.append([item,1])
            else:
                ele=obj.popleft()
                # print(ele)
                if(item-ele[0]==1):
                    obj.append([item,ele[1]+1])
                else:
                    return False
            while(len(obj)>0 and obj[-1][1]==groupSize):
                obj.pop()
        return (len(obj)==0)

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        N, groupSize = list(map(int, input().split()))
        hand = list(map(int, input().split()))
        ob = Solution()
        res = ob.isStraightHand(N, groupSize, hand);
        print(res)
# } Driver Code Ends