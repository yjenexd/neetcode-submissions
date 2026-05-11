class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        hashMap = {}
        length = len(board)
        for i in range(length):
            for j in range(length):
                if (board[i][j] == "."):
                    continue
                else:
                    hashMap[(i, j)] = board[i][j]

        ##check rows
        for i in range(length):
            row = {}
            for j in range(length):
                number = hashMap.get((i,j))
                if number == None:
                    continue
                if number in row:
                    return False
                else:
                    row[number] = 1
        ##check col
        for i in range(length):
            col = {}
            for j in range(length):
                number = hashMap.get((j,i))
                if number == None:
                    continue
                if number in col:
                    return False
                else:
                    col[number] = 1

        ##check square
        for i in range(0, length, 3):
            for j in range(0, length, 3):
                square = {}
                for k in range(3):
                    for l in range(3):
                        number = hashMap.get((i + k, j + l))
                        if number == None:
                            continue
                        if number in square:
                            return False
                        else:
                            square[number] = 1
        print("flag")
        return True





#turn lst into hashmap of ((row, col), num)
# check all numbers in the same row, if there are any duplicates (O(N^2))
# check all numbers in the same col, if there are any duplicates (O(N^2))
# check all the squares



        