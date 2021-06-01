from ursina import *
import numpy as np
from tensorflow.keras.models import load_model

model = load_model('models/20201213_202430.h5')
w, h = 20, 20

def getComMapIJFromAI(str_info400):
    input = np.zeros(20*20)
    
    for i in range(len(str_info400)):
        input[i]=str_info400[i:i+1]
        
    input[input == 2] = -1
    input = np.reshape(input,(1,20,20,1))
    
    output = model.predict(input).squeeze()
    
    output = output.reshape((h, w))
    
    # 인공지능이 놓은자리 검증
    for i in range(len(str_info400)):
        temp_ij =str_info400[i:i+1]
        if temp_ij == "2" or temp_ij == "1":
            output[i] = 0
        
    output_y, output_x = np.unravel_index(np.argmax(output), output.shape)
    
    return output_y, output_x


str_info400 = "0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000002200000000000020220210000000000000010121100000000000000211112000000000000000012100000000000000002111120000000000000002020200000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"

getComMapIJFromAI(str_info400)