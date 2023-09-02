#!/usr/bin/python3
"""
returns the perimeter of an island
described in grid
"""


def island_perimeter(grid):
    """
    finds island perimeter
    """
    rowNo, indexNo = (0, 0,)
    totP, rowP, itemP = (0, 0, 4,)
    for row in grid:
        # print(f"row: {row};\n row number: {rowNo}\n\n")
        indexNo = 0
        for item in row:
            switch = 0
            if (item == 0):
                pass
            else:
                switch = 1
                # print(f"found one at row {rowNo} and index {indexNo}\n")
                if rowNo < (len(grid) - 1):
                    if (grid[rowNo + 1][indexNo] == 1):
                        # print("down one\n")
                        itemP -= 1
                        # print(f"then row perimeter {itemP}\n")
                if rowNo > 0:
                    if (grid[rowNo - 1][indexNo] == 1):
                        # print("up one")
                        itemP -= 1
                        # print(f"then row perimeter {itemP}\n")
                if indexNo < (len(row) - 1):
                    if (row[indexNo + 1] == 1):
                        # print("right one")
                        itemP -= 1
                        # print(f"then row perimeter {itemP}\n")
                if indexNo > 0:
                    if (row[indexNo - 1] == 1):
                        # print("left one")
                        itemP -= 1
                        # print(f"then row perimeter {itemP}\n")
            indexNo += 1
            if itemP == 4 and switch == 0:
                # print("dint switch")
                itemP = 0
            # print(f"item perimeter: {itemP}")
            rowP += itemP
            itemP = 4
        # print(f"this row : {row} , whose current perimeter: {rowP}")
        rowNo += 1
        totP += rowP
        # print(f"total perimeter so far: {totP}")
        rowP = 0

    return(totP)
