class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        #Union-Find
        n = len(M)
        count = n
        data = [i for i in range(n)]
        for i in range(n):
            r1 = find(data,i)
            for j in range(i+1,n):
                r2 = find(data,j)
                if r1 != r2 and M[i][j] == 1:
                    count -= 1
                    data[r2] = r1
        return count
    
def find(data,i):
    if i != data[i]:
        data[i] = find(data, data[i])
    return data[i]

"""M = [[1,1,0,0,0,0],
     [1,1,1,1,0,0],
     [0,1,1,0,0,0],
     [0,1,0,1,0,0],
     [0,0,0,0,1,1],
     [0,0,0,0,1,1]]"""
