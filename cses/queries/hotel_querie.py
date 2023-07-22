h, g = [int(i) for i in input().split(" ")]

hotels = [int(i) for i in input().split(" ")]
groups = [int(i) for i in input().split(" ")]
reserved = []

for group in groups:
    for index, hotel in enumerate(hotels):
        if group <= hotel:
            hotels[index] -= group
            reserved.append(index +1)
            break

        elif group > max(hotels):
            reserved.append(0)
            break

print(reserved)