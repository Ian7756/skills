import random

com = ""

mine = input("홀짝을 고르시오")
# print(mine)

result = ""

rnd = random.randint(0,1)

if rnd == 0:
    com = "홀"
else:
    com = "짝"

if com == mine :
    result = "이김"
else :
    result = "짐"    

print("컴:{}".format(com))
print("나:{}".format(mine))
print("결과:{}".format(result))


