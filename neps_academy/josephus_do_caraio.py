#Incompleto

n = 1337
k = 1313
childs = [i+1 for i in range(n)]
removed = []
for i in range(0, n, 2):
    removed.append(childs[k])
    
    
    k= k % n

print(removed[-1])
