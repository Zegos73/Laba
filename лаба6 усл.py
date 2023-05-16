import math

points = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]
max_distance = 3.0
def are_points_on_line(points):
    x1, y1 = points[0]
    x2, y2 = points[1]
    for i in range(2, len(points)):
        x, y = points[i]
        if (y2 - y1) * (x - x2) != (y - y2) * (x2 - x1):
            return False
    return True

def distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def generate_combinations(points, k):
    if k == 0:
        yield []
    else:
        for i in range(len(points)):
            for comb in generate_combinations(points[i+1:], k-1):
                yield [points[i]] + comb

for i in range(2, len(points) + 1):
    for comb in generate_combinations(points, i):
        distances = [distance(comb[j], comb[k]) for j in range(i) for k in range(j+1, i)]
        if all(d <= max_distance for d in distances):
            line_points = list(comb)
            if are_points_on_line(line_points):
                print("Точки", line_points, "лежат на одной прямой")
