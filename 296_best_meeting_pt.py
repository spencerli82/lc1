def minTotalDistance(grid):
    row_sum = map(sum, grid)
    col_sum = map(sum, zip(*grid))  # syntax sugar learned from stefan :-)

    def minTotalDistance1D(vec):
        i, j = 0, len(vec)-1
        d, left, right = 0, vec[i], vec[j]
        while i != j:
            if left < right:
                d += left
                i += 1
                left += vec[i]
            else:
                d += right
                j -= 1
                right += vec[j]
        return d

    return minTotalDistance1D(row_sum) + minTotalDistance1D(col_sum)

def minTotalDistance2(grid):
    total = 0
    for g in grid, zip(*grid):
        X = []
        for x, row in enumerate(g):
            X += [x] * sum(row)
        total += sum(abs(x - X[len(X)/2])
                     for x in X)
    return total

grid = [[1,0,0,0,1],[0,0,0,0,0],[0,0,1,0,0]]
print minTotalDistance2(grid)
