# Dado uma sequencia de n numeros, fazer q queries com uma definida condição:
# Somar os itens dos índices indicados

n, q = [int(x) for x in input().split(" ")]
nums = [int(x) for x in input().split(" ")]

comand = []
ordered_queries = []
for i in range(q):
    comand.append([int(a) for a in  input().split(" ")])
    
for i, f in comand:
    summatory = sum(nums[i-1 : f])
    ordered_queries.append(sum)

print(ordered_queries)