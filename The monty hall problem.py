import random

result = 0
iteration = 1000000

for i in range(iteration):
    doors=["sheep","sheep","car"]
    random.shuffle(doors)
    yourchoose=doors[random.randint(0,2)]
    doors.remove("car")
    if yourchoose in doors:
      doors.remove(yourchoose)
      result +=1
print(result/iteration)
