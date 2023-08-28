import numpy as np
import matplotlib.pyplot as plt

class birthday_Problem():
    data_range = range(1,367)
   
    
    def __init__(self,run_times):
        self.run_times = run_times
    

    
    def get_Data(self,data_range,number_p):
        Data = np.random.choice(data_range,number_p,replace=True)
        return Data
        
    def if_same(self,Data):
        if len(Data)>len(set(Data)):
            return True
        
    def run(self,run_times):
        probs=[]
        count = 0
        for number_p in range(1,101):
            for i in range(run_times):
                Data=self.get_Data(self.data_range,number_p)
                if self.if_same(Data):
                    count+=1
            probs.append(count/run_times)
        return probs
    
b_P=birthday_Problem(1000)
probs=b_P.run(1000)
n=range(1,101)
plt.plot(n,probs)
plt.show


import numpy as np
import matplotlib.pyplot as plt

class birthday_Problem():
    data_range = np.arange(1,366)
   
    
    def __init__(self,run_times,group_sizes):
        self.run_times = run_times
        self.group_sizes = group_sizes
    
    def individual_group(self,group_sizes):
        count = 0
        for i in range(self.run_times):
            Data = np.random.choice(self.data_range,size=group_sizes,replace=True)
            if self.if_same(Data):
                count+=1
        return count
        
    def if_same(self,Data):
        if len(Data)>len(set(Data)):
            return True
        
    def run(self):
        probs = []
        for size in self.group_sizes:
            count =self.individual_group(size)
            prob = count/self.run_times
            probs.append(prob)
        return probs
    

group_sizes=np.arange(1,101)
b_P=birthday_Problem(10000,group_sizes)
probs=b_P.run()
plt.plot(n,probs)
plt.show
    
            
    
            
    
