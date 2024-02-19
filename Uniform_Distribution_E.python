import numpy as np
import matplotlib.pyplot as plt

class uniform_Distribution:
    def __init__(self,size):
        self.size=size
        
    def construct_Data(self,size):
        Data = 0
        for i in range(size):
            Data += 1/size*np.random.uniform(0,1)
        return Data

u_D=uniform_Distribution(1000)
print(u_D.construct_Data(1000))
