class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        arr=[[0,0] for _ in range(n)]
        for item in bookings:
            a,b,c=item
            arr[a-1][0]+=c
            arr[b-1][1]+=c
        ans=[]
        s=0
        for item in arr:
            s+=item[0]
            ans.append(s)
            s-=item[1]
        return ans