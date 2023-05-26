class Solution(object):
    
    def findDiagonalOrder(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        res=[]
        def upside(mat,row=0,col=0):
            res.append(mat[row][col])

            if col==len(mat[0])-1:
                if row==len(mat)-1:
                    return res
                row += 1
                return downside(mat,row,col)

            while col<=row:
                col += 1
                row -= 1
                if row == -1:
                    row += 1
                    return downside(mat,row,col)
                return upside(mat,row,col)
            
            if col < len(mat[0])-1:
                col += 1
                return downside(mat,row,col)
            else:
                row += 1
                return downside(mat,row,col)
    
        def downside(mat,row,col):
            res.append(mat[row][col])

            if row==len(mat)-1 and col==len(mat[0])-1:
                return res

            while row<=col:
                row += 1
                col -= 1
                return downside(mat,row,col)
            
            if row < len(mat)-1:
                row += 1
                return upside(mat,row,col)
            else:
                col += 1
                return upside(mat,row,col)
        if len(mat)==1:
            return mat[0]

        return upside(mat,row=0,col=0)

                

mat = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
a=Solution()
a.findDiagonalOrder(mat)