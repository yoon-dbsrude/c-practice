def flatten(results):
    rows=[]

    for row in results:
        cells=[]
        for cell in row:
            cells.append(cell)
        rows.append(tuple(cells))
    return tuple(rows)

a=flatten([[1,2,3],[4,5,6]])
print(a)