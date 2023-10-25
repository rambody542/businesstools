import random

random_number = random.randint(1, 100)

#print(random_number)

game_count = 1

while True:
  my_number = int(input("1~100 사이의 숫자를 입력하세요:"))
  
  if my_number > random_number:
    print("Down")
  elif my_number < random_number:
    print("Up")
  elif my_number == random_number:
    print("축하합니다. {} 회 만에 맞췄습니다.".format(game_count))
    break
  32
  game_count = game_count + 1
  
