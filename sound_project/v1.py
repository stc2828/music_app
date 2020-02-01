from pysine import sine
from multiprocessing import Process
import math
import time

def sing1():
    #sine(frequency=220.0, duration=2.0)
    print("j")
    print("j")
def sing2():
    #sine(frequency=440.0, duration=2.0)
    print("j")
def sing3():
    #sine(frequency=880.0, duration=1.0)
    print("j")

p1 = Process(target=sing1)
#p1 = Process(target = sing1, args=())
p1.start()
p1.join()

#sine(frequency=220.0, duration=1.0)
#sine(frequency=440.0, duration=1.0)
#sine(frequency=880.0, duration=1.0)
  
print("Done!")

b = 261.6

#ll = [0, 2, 4, 5, 7, 9, 11, 12]
ll = [0, 2, 4, 6, 7, 9, 11, 13, 15, 16]
#my scale
# 1     2     3     4  5     6     7     8     9  1
# 1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16  1 
def scale(l, d):
    for i in range(l+1):
        f = b*2**(1.0/l*i)
        print(f)
    for i in range(l+1):
            
        f = b*2**(1.0/l*i)
        if i in ll:
            sine(f, d)
            a = 3
        #sine(f, d)

#scale(30, 0.5)


sheet = []

#make music here

##sheet.append([200, 0.2])
##sheet.append([400, 0.2])
##sheet.append([200, 0.2])
##sheet.append([400, 0.2])
##sheet.append([200, 0.2])
##sheet.append([300, 0.5])
##sheet.append([-1, 0.1])
##sheet.append([300, 0.5])
##sheet.append([-1, 0.1])
##sheet.append([300, 0.5])
sheet.append([1, 0.5])
sheet.append([-1, 0.1])
sheet.append([1, 0.5])
sheet.append([-1, 0.1])
sheet.append([8, 0.5])
sheet.append([-1, 0.1])
sheet.append([8, 0.5])
sheet.append([-1, 0.1])
sheet.append([10, 0.5])
sheet.append([-1, 0.1])
sheet.append([10, 0.5])
sheet.append([-1, 0.1])
sheet.append([8, 1.1])
sheet.append([-1, 0.1])
sheet.append([6, 0.5])
sheet.append([-1, 0.1])
sheet.append([6, 0.5])
sheet.append([-1, 0.1])
sheet.append([5, 0.5])
sheet.append([-1, 0.1])
sheet.append([5, 0.5])
sheet.append([-1, 0.1])
sheet.append([3, 0.5])
sheet.append([-1, 0.1])
sheet.append([3, 0.5])
sheet.append([-1, 0.1])
sheet.append([1, 0.5])
sheet.append([-1, 0.1])

##for i in sheet:
##    if i[0] == -1:
##        time.sleep(i[1])
##    elif i[0] < 13:
##        f = b*2**(1.0/12*(i[0]-1))
##        sine(f, i[1])
##    else:
##        sine(i[0], i[1])

#sine(300, 10)

#western scale
# 1     2     3  4     5     6     7  1
# 1  2  3  4  5  6  7  8  9 10 11 12  1


#chinese scale
#       4     5     1        2     3        4     5     1        2     3 
# 1  2  3  4  5  6  7  8  9 10 11 12  1  2  3  4  5  6  7  8  9 10 11 12 

#my scale
# 1     2     3     4  5     6     7     8     9  1
# 1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16  1    
