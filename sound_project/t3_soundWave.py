from pysine import sine
from multiprocessing import Process
import math
import time

def sing(f, d):
    sine(f, d)

def cord(a, d):
    p = []
    for i in a:
        temp = Process(target=sing, args=(i, d,))
        p.append(temp)
        temp.start()

    #return list of processes for join()
    return p


#TESTS
def littleStar(sheet):
    sheet.append([[261, 523], 1, 0])
    sheet.append([[261, 523], 1, 1])
    sheet.append([[329, 783], 1, 2])
    sheet.append([[261, 783], 1, 3])
    
    sheet.append([[349, 880], 1, 4])
    sheet.append([[261, 880], 1, 5])
    sheet.append([[329], 1, 6])
    sheet.append([[783], 2, 6])
    sheet.append([[261], 1, 7])

    return sheet

def sheetTest():
    processes = []
    
    #generate sheet
    sheet = []
    #sheet entry format: [[cords], duration, time]
    sheet = littleStar(sheet)


    #play the sheet
    l = len(sheet)
    for i in range(l):
        processes += cord(sheet[i][0], sheet[i][1])

        if i < l-1:
            time.sleep(sheet[i+1][2]-sheet[i][2])


    #wait for all process to finish
    for i in processes:
        i.join()
    print("done")


def cfTest():
    print("from 261 step 1:277.2, 2:293.7, 3:311.1")
    
    for i in range(11):
        print("playing frequency 261.63 +", 262+(i**2)/2)
        cord([261.63, 262+(i**2)/2], 5)
        time.sleep(4.9)

def cfTest2():
    
    for i in range(80):
        if i%10 ==0:
            print("playing frequency 261.63 +", 262+(i**2)/2)
        cord([261.63, 262+(i**2)/10], 0.5)
        time.sleep(0.4)

def cfTest3():
    
    for i in range(80):
        if i%10 ==0:
            print("playing frequency 261.63 +", 262+(i**2)/2)
        cord([261.63, 262+(i**(-12))/10], 0.5)
        time.sleep(0.4)
        
#MAIN
if __name__ == '__main__':
    cord([261.63, 262.08], 10)
    #sheetTest()
    #cfTest2()



    
