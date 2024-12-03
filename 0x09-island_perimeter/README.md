# 0. Island Perimeter

This project focuses on calculating the perimeter of an island represented in a grid. It tests your understanding of algorithms, 2D arrays (matrices), and conditional logic. By the end of the project, you will be able to navigate grids, analyze adjacent cells, and apply logical operations to solve geometric problems efficiently.

---

## **Concepts Needed**

### **1. 2D Arrays (Matrices)**  
Understanding 2D arrays is crucial, as the grid representing the island is stored in this format. You will need to:
- **Access Elements**: Use nested loops to traverse rows and columns.
- **Navigate Adjacent Cells**: Identify neighboring cells (up, down, left, right) relative to the current cell.

### **2. Conditional Logic**  
The perimeter of the island depends on identifying boundaries or edges of land cells. You must:
- Check if a cell is **land** (value = 1).
- Determine if adjacent cells are either **water** (value = 0) or out of bounds, which contributes to the perimeter.

### **3. Counting Techniques**  
Develop a systematic method to:
- Count edges of a cell contributing to the perimeter.
- Sum these counts for all land cells.

### **4. Problem-Solving Strategies**  
Breaking down the task:
1. **Identify Land Cells**: Traverse the grid and locate cells with a value of 1.
2. **Calculate Contribution**: For each land cell, check its neighbors and add to the perimeter count accordingly.
3. **Combine Results**: Aggregate the contributions from all land cells.

### **5. Python Programming Skills**  
Key programming concepts to use:
- **Nested Loops**: To iterate through the rows and columns of the grid.
- **Conditionals**: To check the status of each cell and its neighbors.
- **Boundary Checks**: To handle cells at the edges of the grid gracefully.

---

## **Problem Description**

Given a grid (2D array) where:
- `0` represents water.
- `1` represents land.

The task is to calculate the perimeter of the island.  
The island:
- Is **one contiguous block** of land.
- Has no lakes (water surrounded by land).

---

## **Steps to Solve**

1. **Traverse the Grid**  
   Use nested loops to iterate over each cell of the grid.

2. **Identify Land Cells**  
   Check if the current cell has a value of 1.

3. **Calculate Perimeter Contribution**  
   For each land cell:
   - Check the cells above, below, left, and right.
   - Add 1 to the perimeter for every water cell or grid boundary.

4. **Sum Up the Perimeter**  
   Aggregate the contributions from all land cells to get the total perimeter.

---

## **Example**

### **Input Grid**
```python
grid = [
    [0, 1, 0, 0],
    [1, 1, 1, 0],
    [0, 1, 0, 0],
    [1, 1, 0, 0]
]
```

### **Output**
The perimeter of the island is **16**.

### **Visualization**
- Each `1` contributes to the perimeter based on its surroundings.
- The top-left `1` contributes 3 edges (top, left, right).
- Repeat this logic for all `1`s in the grid.

---

## **Implementation**

Here’s a simple Python implementation:

```python
def island_perimeter(grid):
    rows, cols = len(grid), len(grid[0])
    perimeter = 0
    
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:  # Land cell
                # Check all four directions
                if i == 0 or grid[i-1][j] == 0:  # Up
                    perimeter += 1
                if i == rows-1 or grid[i+1][j] == 0:  # Down
                    perimeter += 1
                if j == 0 or grid[i][j-1] == 0:  # Left
                    perimeter += 1
                if j == cols-1 or grid[i][j+1] == 0:  # Right
                    perimeter += 1
    
    return perimeter
```

---

## **Key Takeaways**
- Understand grid traversal and boundary conditions.
- Use logic to calculate contributions to the perimeter.
- Test with different inputs to validate the solution.
