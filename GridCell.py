def get_grid(column, row, distance_threshold, grid):
    """
    Range over the number of rows and columns, take the distance of each
    coordinate in the grid from the current cell (row position, column position).
    If the distance is less than the threshold, increase the count. If there are
    multiple positive cells sharing a cell, add it to the shared cells dictionary.
    
    Parameters
    ----------
    column : int
        The number of columns
    row : int
        The number of rows
    distance_threshold: int
        The threshhold is the maximum distance
    grid: list[list[int]]
        A list of x and y coordinates
        
    Returns
    -------
    count :
        The count fo positive cells within the given threshold.
    shared_cells:
        If there are multiple positive values within one cell it will
        return the coordinates for both the positive values.

    """
    if row < 1 or column < 1 or distance_threshold < 1:
        return "There is a zero input for row, column, or distance threshold. Ensure to add a value greater than 1."
    shared_cells = {}
    count = 0
    for i in range(row):
        for j in range(column):
            coordinates_within = []
            for pos in range(len(grid)):
                y = i - grid[pos][1]
                x = j - grid[pos][0]
                dis_to_pos = abs(y) + abs(x)

                if distance_threshold >= dis_to_pos:
                    # count +=1
                    # break
                    coordinates_within.append((grid[pos][0], grid[pos][1]))
            
            if len(coordinates_within) > 0:
                count +=1

            if len(coordinates_within) > 1:
                shared_cells[(i,j)] = coordinates_within

    print(shared_cells)
    return count

if __name__ == '__main__':
    # Example 1:
    print("Example 1:")
    print(get_grid(11,11, 3, [[5 ,5]]))
    # Example 2:
    print("\nExample 2:")
    print(get_grid(11, 11, 3, [[1,5]]))
    # Example 3: 
    print("\nExample 3:")
    print(get_grid(11, 11, 2, [[2,3],[4,7]]))
    # Example 4: 
    print("\nExample 4:")
    print(get_grid(11, 11, 2, [[3,3],[5,4]]))

    # # ignoring a 0 for row
    print("\nExceptions:\n\nIgnoring because the row is 0:")
    print(get_grid(11, 0, 3, [[5,5]]))
    # # ignoring a 0 for column
    print("\nIgnoring because the column is 0:")
    print(get_grid(0, 11, 3, [[5,5]]))
    # # ignoring a 0 for n
    print("\nIgnoring because the threshold is 0:")
    print(get_grid(11, 11, 0, [[5,5]]))