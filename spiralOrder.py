class Solution:
    def spiralOrder(self, matrix):
        if len(matrix)==0:
            return []
        if len(matrix)==1:
            return matrix[0]
        if len(matrix[0])==1:
            return [x[0] for x in matrix]
        res=matrix[0].copy()
        for i in range(1,len(matrix)):
            res.append(matrix[i][-1])
        res.pop()
        for j in range(1,len(matrix[0])):
            res.append(matrix[-1][-j])

        for t in range(1,len(matrix)):
            res.append(matrix[-t][0])
        if len(matrix)==2:
            return res
        elif len(matrix[0])==2:
            return res
        else:
            new_matrix = [l[1:-1] for l in matrix]
            new_matrix = new_matrix[1:-1]

            res.extend(self.spiralOrder(new_matrix))
        return res

so=Solution()
matrix=[[1,2,3],[4,5,6],[7,8,9]]

print(so.spiralOrder(matrix))