#!/usr/bin/python3
"""
returns the perimeter of an island
described in grid
"""
def island_perimeter(grid):
    rowNo, indexNo = (0, 0,)
    for row in grid:
        print("row:")
        print(row)
        print("row number: ")
        print(rowNo)
        rowNo += 1
        indexNo = 0
        for item in row:
#            print("item:")
#            print(item)
#            print(indexNo)
            indexNo += 1
            if (item == 0):
                pass
            else:
                print("1 item:")
                print(item)
                if rowNo < (len(row) - 1):
                    if (grid[rowNo + 1][indexNo] == 1):
                        print("down one")
                if rowNo > 0:
                    if (grid[rowNo - 1][indexNo] == 1):
                        print("up one")
                if indexNo < (len(row) - 1):
                    if (row[indexNo + 1] == 1):
                        print("right one")
                if indexNo > 0:
                    if (row[indexNo - 1] == 1):
                        print("left one")
