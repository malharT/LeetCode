class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        i = 0
        while i < len(matrix)//2:
            copy_array = matrix[i][i:len(matrix)-i].copy()
            print(copy_array)
            for j in range(len(copy_array)):
                temp = matrix[i + j][-i - 1]
                matrix[i + j][-i - 1] = copy_array[j]
                copy_array[j] = temp
            print(copy_array)
            for j in range(1,len(copy_array)):
                temp = matrix[-i-1][-j-i-1]
                matrix[-i-1][-j-i-1] = copy_array[j]
                copy_array[j] = temp
            print(copy_array)
            for j in range(1, len(copy_array)):
                temp = matrix[i+len(copy_array)-1-j][i]
                matrix[i+len(copy_array)-1-j][i] = copy_array[j]
                copy_array[j] = temp
            print(copy_array)
            for j in range(1, len(copy_array)):
                temp = matrix[i][i+j]
                matrix[i][i+j] = copy_array[j]
            print(copy_array)
            i += 1
        return matrix
