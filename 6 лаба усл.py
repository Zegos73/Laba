# На плоскости задано К точек. Сформировать все возможные варианты выбора множества точек из них на проверку того, что они принадлежат одной прямой.
points = [(1, 1), (3, 3), (5, 5), (8, 8), (9, 9), (12,12),(101,101)]

def are_points_on_line(points):
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

max_points_on_line = 0  
max_line_points = []  

for i in range(2, len(points) + 1):
    for comb in generate_combinations(points, i):
        line_points = list(comb)
        if all(point[0] % 2 != 0 and point[1] % 2 != 0 for point in line_points):
            if are_points_on_line(line_points):
                odd_points_count = count_odd_points_on_line(line_points)
                if odd_points_count > max_points_on_line:
                    max_points_on_line = odd_points_count
                    max_line_points = line_points

print("Точки", max_line_points, "лежат на одной прямой и содержат максимальное количество точек с нечетными координатами:", max_points_on_line)
