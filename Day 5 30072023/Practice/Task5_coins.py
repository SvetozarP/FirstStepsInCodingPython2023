coins_return = round(float(input()),2)
coins_counter = 0
returned = False

while coins_return - 2 >= 0 and not returned:
    coins_return = round(coins_return -2, 2)
    coins_counter += 1
    if coins_return < 0.01:
        returned = True

while coins_return - 1 >= 0 and not returned:
    coins_counter += 1
    coins_return = round(coins_return - 1, 2)
    if coins_return < 0.01:
        returned = True

while coins_return - 0.5 >= 0 and not returned:
    coins_return = round(coins_return - 0.5,2)
    coins_counter += 1
    if coins_return < 0.01:
        returned = True

while coins_return - 0.2 >= 0 and not returned:
    coins_return = round(coins_return - 0.2,2)
    coins_counter += 1
    if coins_return < 0.01:
        returned = True

while coins_return - 0.1 >= 0 and not returned:
    coins_return = round (coins_return - 0.1,2)
    coins_counter += 1
    if coins_return < 0.01:
        returned = True

while coins_return - 0.05 >= 0 and not returned:
    coins_return = round(coins_return - 0.05,2)
    coins_counter += 1
    if coins_return < 0.01:
        returned = True

while coins_return - 0.02 >= 0 and not returned:
    coins_return = round(coins_return - 0.02,2)
    coins_counter += 1
    if coins_return < 0.01:
        returned = True

while coins_return - 0.01 >= 0 and not returned:
    coins_return = round(coins_return - 0.01,2)
    coins_counter += 1
    if coins_return <0.01:
        returned = True

if returned:
    print(coins_counter)