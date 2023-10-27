import tkinter as tk

def are_points_on_line(points):
    if len(points) < 2:
        return True
    
    x1, y1 = points[0]
    x2, y2 = points[1]
    for i in range(2, len(points)):
        x, y = points[i]
        if (y2 - y1) * (x - x2) != (y - y2) * (x2 - x1):
            return False
    return True

def generate_combinations(points, k):
    if k == 0:
        yield []
    else:
        for i in range(len(points)):
            for comb in generate_combinations(points[i+1:], k-1):
                yield [points[i]] + comb

def count_odd_points_on_line(line_points):
    odd_points = [point for point in line_points if point[0] % 2 != 0 and point[1] % 2 != 0]
    return len(odd_points)

def process_points():
    points_str = entry.get()
    points_list = eval(points_str)
    
    max_points_on_line = 0
    max_line_points = []

    for i in range(2, len(points_list) + 1):
        for comb in generate_combinations(points_list, i):
            line_points = list(comb)
            if all(point[0] % 2 != 0 and point[1] % 2 != 0 for point in line_points):
                if are_points_on_line(line_points):
                    odd_points_count = count_odd_points_on_line(line_points)
                    if odd_points_count > max_points_on_line:
                        max_points_on_line = odd_points_count
                        max_line_points = line_points

    result_str = f"Точки {max_line_points} лежат на одной прямой и содержат максимальное количество точек с нечетными координатами: {max_points_on_line}"
    output_entry.delete(0, tk.END)
    output_entry.insert(0, result_str)

root = tk.Tk()
root.title("Проверка точек на прямую")

input_frame = tk.Frame(root)
input_frame.pack(pady=10)

label = tk.Label(input_frame, text="Введите точки (x, y):")
label.pack(side=tk.LEFT)

entry = tk.Entry(input_frame, width=50)
entry.pack(side=tk.LEFT)

output_frame = tk.Frame(root)
output_frame.pack(pady=10)

output_label = tk.Label(output_frame, text="Результат:")
output_label.pack(side=tk.LEFT)

output_entry = tk.Entry(output_frame, width=50)
output_entry.pack(side=tk.LEFT)

button = tk.Button(root, text="Проверить точки", command=process_points)
button.pack(pady=10)

root.mainloop()
