import random
'''
Created on 2021. 6. 1.

@author: IAN
'''
# 파이썬은 음 순서가 중요함.. 일단 그래... 출력은 저렇게 하는거시야.
print("hello python")
print("컴:{}".format("44"))
# 길이 측정 
#len()

# range()는 배열 만들어주는 메서드
# 이터레이터 식 포문
for i in range(5):
    print(i)

# if 문
a = 1.1
if a < 0 : 
    print("거짓")
elif a > 1 :
    print("크긴하네...")
else:
    print("와우")

# random
rnd = random.randint(0,1)
print(rnd)

