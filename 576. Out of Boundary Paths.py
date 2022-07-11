class Solution(object):
    def my_sum(self, *nested_lists):
        return [[sum(items) for items in zip(*zipped_list)] for zipped_list in zip(*nested_lists)]

    def traverse_and_record(self, old_array, new_array, x_boundary, y_boundary):
        for column in range(y_boundary):
            for row in range(x_boundary):
                if row - 1 > -1:
                    new_array[row][column] += (old_array[row - 1][column])
                if (row + 1) < x_boundary:
                    new_array[row][column] += (old_array[row + 1][column])
                if column - 1 > -1:
                    new_array[row][column] += (old_array[row][column - 1])
                if column + 1 < y_boundary:
                    new_array[row][column] += (old_array[row][column + 1])

    def findPaths(self, m, n, maxMove, startRow, startColumn):
        """
        :type m: int
        :type n: int
        :type maxMove: int
        :type startRow: int
        :type startColumn: int
        :rtype: int
        """
        old_array = []
        for row in range(m):
            old_array.append([0]*n)
        old_array[startRow][startColumn] = 1
        count = 0
        
        if maxMove > 0:
            for column in range(n):
                count += old_array[0][column]
            for row in range(m):
                count += old_array[row][0]
            for column in range(n):
                count += old_array[m-1][column]
            for row in range(m):
                count += old_array[row][n-1]
        for moves in range(maxMove-1):
            new_array = []
            for column in range(m):
                new_array.append([0]*n)
            print(old_array)
            self.traverse_and_record(old_array, new_array, m, n)
            for row in range(m):
                for column in range(n):
                    old_array[row][column] = new_array[row][column]
            for column in range(n):
                count += old_array[0][column]
            for row in range(m):
                count += old_array[row][0]
            for column in range(n):
                count += old_array[m-1][column]
            for row in range(m):
                count += old_array[row][n-1]
        print(old_array)
        
        return count%(int(pow(10,9)) + 7)