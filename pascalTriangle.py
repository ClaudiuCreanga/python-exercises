def pascalTriangle(n_rows):
    results = [] # will be a list of lists where each a row is a list [[1],[1,1],[1,2,1]]
    for _ in range(n_rows): # _ variable suggests that it is not used in the loop
        row = [1] # a starter 1 in the row because every row starts with 1
        if results: # then we're in the second row or beyond
            last_row = results[-1] # get the last row
            # duplicate the last row except the first item and zip them into pairs that at the end will be summed
            # [1,3,3,1] and [3,3,1] become [[1,3],[3,3],[3,1]] with the sum returning [4,6,4]
            row.extend([sum(pair) for pair in zip(last_row, last_row[1:])])
            row.append(1) # every row ends with 1
        results.append(row) # add the row to the results.
    return results
for i in pascalTriangle(6):
    print(i)

def pascal(c,r):
    if c == 0 or c == r: # if column is 0 or column is equal to row then it is a 1
        return 1
    return pascal(c-1,r-1) + pascal(c, r-1) # return the sum of the 2 elements from previous row that make the next number

print(pascal(2,5))