class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, points):
        self.points = points

    def are_points_on_line(self):
        x1, y1 = self.points[0].x, self.points[0].y
        x2, y2 = self.points[1].x, self.points[1].y
        for i in range(2, len(self.points)):
            x, y = self.points[i].x, self.points[i].y
            if (y2 - y1) * (x - x2) != (y - y2) * (x2 - x1):
                return False
        return True

    def count_odd_points(self):
        odd_points = [point for point in self.points if point.x % 2 != 0 and point.y % 2 != 0]
        return len(odd_points)

class Combinations:
    @staticmethod
    def generate_combinations(points, k):
        if k == 0:
            yield []
        else:
            for i in range(len(points)):
                for comb in Combinations.generate_combinations(points[i+1:], k-1):
                    yield [points[i]] + comb

points = [Point(1, 1), Point(3, 3), Point(5, 5), Point(8, 8), Point(9, 9), Point(12, 12), Point(101, 101)]

max_points_on_line = 0  
max_line_points = []  

for i in range(2, len(points) + 1):
    for comb in Combinations.generate_combinations(points, i):
        line_points = list(comb)
        if all(point.x % 2 != 0 and point.y % 2 != 0 for point in line_points):
            line = Line(line_points)
            if line.are_points_on_line():
                odd_points_count = line.count_odd_points()
                if odd_points_count > max_points_on_line:
                    max_points_on_line = odd_points_count
                    max_line_points = line_points

print("Точки", [(point.x, point.y) for point in max_line_points], "лежат на одной прямой и содержат максимальное количество точек с нечетными координатами:", max_points_on_line)
