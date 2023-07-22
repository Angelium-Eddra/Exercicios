

qtd_bandejas = int(input())
copos_quebrados = 0

for each in range(qtd_bandejas):
    latas, copos = input().split(" ")
    latas, copos = int(latas), int(copos)
    if latas > copos:
        copos_quebrados += copos

print(copos_quebrados)