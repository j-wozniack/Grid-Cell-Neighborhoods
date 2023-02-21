# Grid Cell Neighborhoods
This python project utilizes the Manhattan distance function to find the neighborhood grid layout when given a distance threshhold.

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

# Assumptions
Rows must be > 0
Columns must be > 0
Distance thresh hold or n must be > 0

# Build Instructions
1. Pull down the code from main
2. Run in terminal: python3 GridCell.py
 

# Project Structure
```
├── README.md
├── GridCell.py

```
