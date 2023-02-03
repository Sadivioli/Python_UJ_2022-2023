import tkinter as tk

def find_largest_rectangle(file_name):
    with open(file_name) as f:
        lines = f.readlines()
    n = int(lines[0])
    square_field = [[int(x) for x in line.split()] for line in lines[1:]]
    # Initialize a 2D array `hist` with the same dimensions as the square field,
    # and set all elements to 0.
    m, n = len(square_field), len(square_field[0])
    hist = [[0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if square_field[i][j] == 0:
                hist[i][j] = hist[i][j-1] + 1 if j > 0 else 1

    # Initialize variables `max_area` and `max_rect` to 0.
    max_area = 0
    max_rect = (0, 0, 0, 0)

    # Iterate through `hist`, and for each row, use the "largest rectangle in histogram"
    # algorithm to find the largest rectangle in that row.
    for i in range(m):
        stack = []
        for j in range(n):
            while stack and hist[i][stack[-1]] >= hist[i][j]:
                h = hist[i][stack.pop()]
                w = j if not stack else j - stack[-1] - 1
                area = h * w
                if area > max_area:
                    max_area = area
                    max_rect = (stack[-1] if stack else 0, i, j, i)
            stack.append(j)
        while stack:
            h = hist[i][stack.pop()]
            w = n if not stack else n - stack[-1] - 1
            area = h * w
            if area > max_area:
                max_area = area
                max_rect = (stack[-1] if stack else 0, i, n, i)
    return max_rect, square_field

def draw_square_field(square_field, max_rect):
    # Create a tkinter window and canvas
    root = tk.Tk()
    root.title("Maxiumum Empty Rectangle")
    canvas = tk.Canvas(root, width=500, height=500)
    canvas.pack()
    
    # Draw the square field
    scaling_factor = 10
    for i in range(len(square_field)):
        for j in range(len(square_field[0])):
            if square_field[i][j] == 1:
                color = "black"
            else:
                color = "white"
            canvas.create_rectangle(i*scaling_factor, j*scaling_factor, (i+1)*scaling_factor, (j+1)*scaling_factor, fill=color)

    # Highlight the found rectangle
    x1, y1, x2, y2 = max_rect
    canvas.create_rectangle(x1*scaling_factor, y1*scaling_factor, x2*scaling_factor, y2*scaling_factor)
    
    root.mainloop()


# Now calling the function
max_rect, square_field = find_largest_rectangle("z5_input.txt")
print("Largest rectangle:", max_rect)
draw_square_field(square_field, max_rect)