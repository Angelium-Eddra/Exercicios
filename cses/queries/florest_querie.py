n, q = [int(x) for x in input().split(" ")]

florest = []
rect_coordinates = []
rects = []
rect_info = []

for line in range(n):    
    florest.append(["T " if g == "*" else "O " for g in input()])

for rectangle in range(q):
    y1, y2, x1, x2 = input().split(" ")
    coordinates = [int(y1), int(y2), int(x1), int(x2)]
    rect_coordinates.append(coordinates)

# print(florest)

def get_rect_values(y1, x1, y2, x2):
    rect_values = []
    for index_y in florest[y1-1 : y2]:
        rect_values.append([value for value in index_y[x1-1 : x2]])
    return rect_values

for y1, x1, y2, x2 in rect_coordinates:
    rects.append(get_rect_values(y1, x1, y2, x2))

for rect in rects:
    trees = 0
    for line in rect:
        for info in line:
            if info == "T ":
                trees += 1
    rect_info.append(trees)


print(rect_info)