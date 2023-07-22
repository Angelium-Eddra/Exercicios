actual = int(input())
sequence = []

while actual != 1:
    sequence.append(int(actual))
    print(actual)
    if actual % 2 == 0:
        actual /= 2
    else: actual = (actual * 3) + 1

print(sequence)