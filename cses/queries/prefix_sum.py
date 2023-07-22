n, q = [int(x) for x in input().split(" ")]
nums = [int(x) for x in input().split(" ")]
comands = []
list_of_bigger_sums = []

for i in range(q):
    ind, v1, v2 = input().split(" ")
    comands.append([int(ind), int(v1), int(v2)])

for ind, v1, v2 in comands:
    if ind == 1:
        nums[v1-1] = v2
    
    elif ind == 2:
        actual_sum = 0
        bigger_sum = 0
        for num in nums[v1-1 : v2]:
            actual_sum += num
            if actual_sum > bigger_sum:
                bigger_sum = actual_sum 
        list_of_bigger_sums.append(bigger_sum)

print(list_of_bigger_sums)