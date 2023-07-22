# Dado uma sequencia de n numeros, fazer q queries com uma definida condição:
# O menor valor entre os índices indicados

n, q = [int(x) for x in input().split(" ")]
nums = [int(x) for x in input().split(" ")]

comand_range = []
ordered_queries = []

for i in range(q):
    comand_range.append([int(a) for a in  input().split(" ")])

for ini, fsh in comand_range:
    ordered_queries.append(min(nums[ini -1: fsh]))

print(ordered_queries)