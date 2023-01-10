#User function template for Python
from queue import PriorityQueue
class Solution:
	def shortest_distance(self, matrix):
	    
		for i in range(len(matrix)):
		    self.findDis(matrix,i)
	def findDis(self,graph,source):
        visited=[-1 for _ in range(len(graph))]
        visited[source]=0
        obj=PriorityQueue()
        obj.put([0,source])
        while(not obj.empty()):
            cost,node=obj.get()
            for i in range(len(graph)):
                if(i==node or graph[node][i]==-1):
                    continue
                elif(visited[i]==-1 or visited[i]>cost+graph[node][i]):
                    visited[i]=cost+graph[node][i]
                    obj.put([visited[i],i])
        for i in range(len(graph)):
            graph[source][i]=visited[i]

#{ 
 # Driver Code Starts
#Initial template for Python 

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		matrix = []
		for _ in range(n):
			matrix.append(list(map(int, input().split())))
		obj = Solution()
		obj.shortest_distance(matrix)
		for _ in range(n):
			for __ in range(n):
				print(matrix[_][__], end = " ")
			print()
# } Driver Code Ends