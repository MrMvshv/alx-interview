""" pascal_triangle
    returns a nested list representing pascal's of n
"""
def pascal_triangle(n):
    pascal = []
    x = 0

    if n <= 0:
        return pascal
    
    while (n > x):
        if x == 0:
            pascal.append([1])
        elif x == 1:
            pascal.append([1, 1])
        else:
            new = []
            m = 0
            for i in range(x + 1):
                if i == 0 or i == x:
                    new.append(1)
                else:
                    digit = pascal[x - 1][i - 1] + pascal[x - 1][i]
                    new.append(digit)
            pascal.append(new)
        x += 1

    return pascal