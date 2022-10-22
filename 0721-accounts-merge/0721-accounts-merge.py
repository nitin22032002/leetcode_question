class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        d={}
        for j in range(len(accounts)):
            item=accounts[j]
            for i in range(1,len(item)):
                if(item[i] in d):
                    d[item[i]].append(j)
                else:
                    d[item[i]]=[j]
        # print(d)
        graph=[[] for _ in range(len(accounts))]
        for item in d.values():
            for i in range(1,len(item)):
                graph[item[0]].append(item[i])
                graph[item[i]].append(item[0])
        # print(graph)
        ans=[]
        visited=[False for _ in range(len(accounts))]
        for i in range(len(accounts)):
            if(not visited[i]):
                emails=set()
                self.dfs(graph,i,visited,emails,accounts)
                ans.append([accounts[i][0]]+sorted(list(emails)))
        return ans
    def dfs(self,graph,node,visited,email,accounts):
        if(visited[node]):
            return
        else:
            visited[node]=True
            for item in graph[node]:
                self.dfs(graph,item,visited,email,accounts)
            for i in range(1,len(accounts[node])):
                email.add(accounts[node][i])