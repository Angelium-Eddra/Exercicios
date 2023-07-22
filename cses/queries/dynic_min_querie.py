# Dynamic queries: substituir valores e soma de outros

n, q = [int(x) for x in input().split(" ")]
nums = [int(x) for x in input().split(" ")]

comand_list = []



subst_queries = []
min_queries = []

for i in range(q):
    comand_list.append([int(a) for a in  input().split(" ")])

for querie, ini, fnsh in comand_list:
    if int(querie) == 1:
        nums[ini -1] = fnsh
        subst_queries.append({f"old index value: {ini}", f"new value: {fnsh}"})
    
    elif int(querie) == 2:
        min_queries.append(min(nums[ini -1: fnsh]))


print(min_queries)

print(subst_queries)