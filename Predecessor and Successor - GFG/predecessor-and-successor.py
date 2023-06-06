'''
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
'''


# This function finds predecessor and successor of key in BST.
# It sets pre and suc as predecessor and successor respectively
class Solution:
    def findPreSuc(self, root, pre, suc, key):
        ans=[None,None]
        val=self.get(root,key,ans)
        if(val[0] or val[1]):
            return val
        if(ans[0] and ans[0].key>key):
            return None,ans[0]
        elif(ans[1] and ans[1].key!=key):
            return ans[1],None
        return ans[0],None
    def get(self,root,target,pre):
        if(root):
            a,b=self.get(root.left,target,pre)
            if(a or b):
                return a,b
            if(root.key>target):
                # print(pre[1].key,pre[0].key)
                if(pre[1] and pre[1].key!=target):
                    return pre[1],root
                return pre[0],root
            pre[0],pre[1]=pre[1],root
            return self.get(root.right,target,pre)
        return None,None

#{ 
 # Driver Code Starts
import queue

# BST Node
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def buildTree(ip):
    # Corner Case
    if len(ip) == 0 or ip[0] == 'N':
        return None

    # Create the root of the tree
    root = Node(int(ip[0]))

    # Push the root to the queue
    q = queue.Queue()
    q.put(root)

    # Starting from the second element
    i = 1
    while not q.empty() and i < len(ip):
        # Get and remove the front of the queue
        currNode = q.get()

        # Get the current node's value from the string
        currVal = ip[i]

        # If the left child is not null
        if currVal != "N":
            # Create the left child for the current node
            currNode.left = Node(int(currVal))

            # Push it to the queue
            q.put(currNode.left)

        # For the right child
        i += 1
        if i >= len(ip):
            break
        currVal = ip[i]

        # If the right child is not null
        if currVal != "N":
            # Create the right child for the current node
            currNode.right = Node(int(currVal))

            # Push it to the queue
            q.put(currNode.right)

        i += 1

    return root


# Driver program to test above functions
t = int(input())
for _ in range(t):
    s = input()
    root = buildTree(s.split())
    k = int(input())
    pre = None
    succ = None
    ob = Solution()
    pre, succ = ob.findPreSuc(root, pre, succ, k)
    if pre:
        print(pre.key, end=' ')
    else:
        print(-1, end=' ')
    if succ:
        print(succ.key, end=' ')
    else:
        print(-1, end=' ')
    print()

# } Driver Code Ends