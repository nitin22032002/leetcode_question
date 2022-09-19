class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        d={}
        for path in paths:
            path=path.split()
            root=path[0]
            for item in path[1:]:
                item=item.split("(")
                if(item[1] in d):
                    d[item[1]].append(f"{root}/{item[0]}")
                else:
                    d[item[1]]=[f"{root}/{item[0]}"]
        result=[]
        for val in d.values():
            if(len(val)>1):
                result.append(val)
        return result