# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        stack=[]
        oper=[]
        ans=None
        i=0
        while(i<len(s)):
            item=s[i]
            if(item=="["):
                stack.append("[")
                obj=NestedInteger()
                if(len(oper)!=0):
                    oper[-1].add(obj)
                oper.append(obj)
                if(not ans):
                    ans=obj
            elif(item=="]"):
                stack.pop()
                oper.pop()
            elif(item==","):
                pass
            else:
                m=1
                if(s[i]=="-"):
                    m=-1
                    i+=1
                num=0
                while(i<len(s) and s[i]!="," and s[i]!=']'):
                    num=num*10+int(s[i])
                    i+=1
                # print(num,i)
                num*=m
                if(i<len(s)):
                    oper[-1].add(NestedInteger(num))
                    if(s[i]==']'):
                        stack.pop()
                        oper.pop()
                else:
                    oper.append(NestedInteger(num))
                    ans=oper[-1]
            i+=1
        return ans
                    