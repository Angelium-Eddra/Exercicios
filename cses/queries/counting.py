n = int(input())

divisors = []
for i in range(n +1):
    if i == 0:
        pass
    elif n % i == 0:
        divisors.append(i)

print(divisors)
print(len(divisors))