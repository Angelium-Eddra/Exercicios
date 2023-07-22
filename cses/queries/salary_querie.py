n, q = [int(x) for x in input().split(" ")]

salaries = [int(s) for s in input().split(" ")]
commands = []
range_employ_salary = []

for querie in range(q):
    ind, value1, value2 = input().split(" ")
    
    commands.append([ind, int(value1), int(value2)])

print(commands)

for indicator, d, b in commands:
    if indicator == "?":
        count_employ_salary = 0
        for i in range(d, b+1):
            count_employ_salary += salaries.count(i)
        range_employ_salary.append(count_employ_salary)
    
    elif indicator == "!":
        salaries[d -1] = b

print(range_employ_salary)
