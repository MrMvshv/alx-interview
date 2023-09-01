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
        print("row number: " + rowNo)
        rowNo += 1
        indexNo = 0
        for item in row:
            print("item:")
            print(item)
            print(indexNo)
            indexNo += 1