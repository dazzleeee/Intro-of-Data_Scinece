import numpy as np
import matplotlib.pyplot as plt

class Central_limit_theorem():
    def __init__(self,toss_size,data_size):
        self.toss_size = toss_size
        self.data_size = data_size
    def basic(self,toss_size):
        possible_value=[i for i in range(1,7)]
        samples=np.mean(np.random.choice(possible_value,toss_size))
        return samples
  
    def run(self,data_size):
        result = [] 
        for iteration in range(data_size):
            result.append(self.basic(self.toss_size))
        return result
    
toss_size = 1000
data_size = 1000
Clt = Central_limit_theorem(toss_size,data_size)
result = Clt.run(Clt.data_size)
plt.hist(result,bins=50,density=True)
plt.show
        
