import random

com = ""
mine = input("가위,바위,보를 고르시오\n")

gameVar = ["가위","바위","보"]

result = ""

rnd = gameVar[random.randint(0,2)]

if com == mine :
    result = "비김"
elif (com == "가위" and mine == "보") or (com == "바위" and mine == "가위") or (com == "보" and mine == "바위"):
    result = "짐"
else:
    result = "이김" 

print("컴:{}".format(com))
print("나:{}".format(mine))
print("결과:{}".format(result))