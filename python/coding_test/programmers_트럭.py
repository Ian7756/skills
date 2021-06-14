# 파라매터
bridge_length,weight,truck_weights,answer = 2,10,[7,4,5,6],0

# 내 변수들
totalTime, totalWeight, passingTruck,passedTruck = 0,0,[],[]

waitingTruck = truck_weights.copy();
waitingTruck.reverse();

passingTruck.append(0);
totalWeight += truck_weights[0];

i = 1;
while passedTruck.__len__() != truck_weights.__len__():
    # 시간은 언제나 흐른다... 틱톡..
    totalTime += 1;
    
    for j in range(passingTruck.__len__()) :
        passingTruck[j] = passingTruck[j]+1;
    
    if passingTruck[0] == bridge_length :
        passingTruck.pop(0);
        passedTruck.append(waitingTruck.pop(0));
        totalWeight -= passedTruck[passedTruck.__len__()-1]
    
    if i < truck_weights.__len__() and totalWeight + truck_weights[i] <= weight:
        passingTruck.append(0);
        totalWeight += truck_weights[i];
        i += 1;
        
totalTime += 1;
answer = totalTime;
print(answer);
        

