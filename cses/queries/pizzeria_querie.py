# incompleto

n, q = [int(x) for x in input().split(" ")]
prices = [int(x) for x in input().split(" ")]
comands = []
lowest_prices = []

for line in range(q):
    comands.append([int(x) for x in input().split(" ")])

def run_commands(indicator, v1, v2= None):
    if indicator == 1:
        prices[v1] = v2
    
    elif indicator == 2:
        lower_price = 10 ** 9
        for price in prices:
            mod_value = v1 - price if v1 - price >= 0 else (v1 - price) * (-1)
            check_price = prices[v1] + mod_value 
            if check_price < lower_price:
                lower_price = check_price
        lowest_prices.append(lower_price)

for comand in comands:
    if len(comand) == 2:
        indicator, v1 = comand
        run_commands(indicator, v1)
    else: 
        indicator, v1, v2 = comand
        run_commands(indicator, v1, v2)

print(lowest_prices)