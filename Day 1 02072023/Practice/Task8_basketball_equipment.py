annual_price_training_basketball = int(input())

bball_trainers_price = annual_price_training_basketball - annual_price_training_basketball * 0.4
bball_clothing = bball_trainers_price - bball_trainers_price * 0.2
bball_ball = bball_clothing * 0.25
bball_accessor = bball_ball * 0.2

total_price = annual_price_training_basketball + bball_trainers_price + bball_clothing + bball_ball + bball_accessor

print(total_price)
