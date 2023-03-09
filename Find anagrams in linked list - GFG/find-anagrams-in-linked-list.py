#User function Template for python3

class Solution:
    def findAnagrams(self, head, s):
        start=head
        count=[-1 for _ in range(26)]
        for item in s:
            if(count[ord(item)-97]==-1):count[ord(item)-97]=0
            count[ord(item)-97]+=1
        j=head
        prv=None
        ans=[]
        r=0
        while(j):
            if(r==len(s)):
                ans.append(start)
                while(start!=j):
                    count[ord(start.data)-97]+=1
                    start=start.next
                prv.next=None
                r=0
            val=j.data
            prv=j
            if(count[ord(val)-97]>0):
                count[ord(val)-97]-=1
                r+=1
                j=j.next
            else:
                while(count[ord(val)-97]<=0 and j!=start):
                    if(count[ord(start.data)-97]!=-1):
                        count[ord(start.data)-97]+=1
                    r-=1
                    start=start.next
                if(count[ord(val)-97]>0):
                    count[ord(val)-97]-=1
                    r+=1
                else:
                    start=start.next
                j=j.next
        if(r==len(s)):
            ans.append(start)
        return ans
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3

# Node Class
class Node:
    def __init__(self):
        self.data = None
        self.next = None
        
# Linked List Class
class Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None
    def insert(self, data):
        if self.head == None:
            self.head = Node()
            self.tail = self.head
            self.head.data = data
        else:
            new_node = Node()
            new_node.data = data
            new_node.next = None
            self.tail.next = new_node
            self.tail = self.tail.next
            
def printlist(head):
    temp = head
    while temp is not None:
        print(temp.data, end=" ")
        temp = temp.next
    print('')

# Driver Program
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        list1 = Linked_List()
        n = int(input())
        values = list(map(str, input().strip().split()))
        for i in values:
            list1.insert(i)
        s = input()
        res = Solution().findAnagrams(list1.head, s)
        for i in range(len(res)):
            printlist(res[i])
        if len(res) == 0:
            print(-1)
            
# } Driver Code Ends