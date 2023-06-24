import random
import matplotlib.pyplot as plt


def is_point_inside_triangle(new_p, p1, p2, p3):
    denominator = (p2[1] - p3[1])*(p1[0] - p3[0]) + (p3[0] - p2[0])*(p1[1] - p3[1])
    a = ((p2[1] - p3[1])*(new_p[0] - p3[0]) + (p3[0] - p2[0])*(new_p[1] - p3[1])) / denominator
    b = ((p3[1] - p1[1])*(new_p[0] - p3[0]) + (p1[0] - p3[0])*(new_p[1] - p3[1])) / denominator
    c = 1 - a - b

    if 0 < a < 1 and 0 < b < 1 and 0 < c < 1:
        return True
    return False

def generate_point(p1, p2, p3):
    return [random.uniform(p1[0], p2[0]), random.uniform(p1[1], p3[1])]

p1 = [0.0, 0.0]
p2 = [100.0, 0.0]
p3 = [50.0, 80.0]

points = [p1, p2, p3]
plt.scatter([p1[0], p2[0], p3[0]], [p1[1], p2[1], p3[1]])

x_coords, y_coords = [], []

new_point = generate_point(p1, p2, p3)

while not is_point_inside_triangle(new_point, p1, p2, p3):
    new_point = generate_point(p1, p2, p3)


for i in range(100000):
    x_coords.append(new_point[0])
    y_coords.append(new_point[1])

    random_p = points[random.randint(0, 2)]
    new_point = [(new_point[0] + random_p[0]) / 2, (new_point[1] + random_p[1]) / 2]


plt.scatter(x_coords, y_coords, s=1)
plt.show()
