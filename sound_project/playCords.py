from pysine import sine
from multiprocessing import Process
import math
import time

class playCords:
    def __init__(self, sheet):
        self.playSheet(sheet)
        
    def sing(self, f, d):
        sine(f, d)

    def cord(self, a, d):
        p = []
        for i in a:
            temp = Process(target=self.sing, args=(i, d,))
            p.append(temp)
            temp.start()

        #return list of processes to join()
        return p

    def playSheet(self, sheet):
        processes = []
        
        #sheet entry format: [[cords], duration, time]
        #play the sheet
        l = len(sheet)
        for i in range(l):
            processes += self.cord(sheet[i][0], sheet[i][1])

            if i < l-1:
                time.sleep(sheet[i+1][2]-sheet[i][2])

        #wait for all process to finish
        for i in processes:
            i.join()
            


if __name__ == '__main__':
    sheet = []
    sheet.append([[261, 523], 1, 0])
    sheet.append([[261, 523], 1, 1])
    sheet.append([[329, 783], 1, 2])
    sheet.append([[261, 783], 1, 3])
    a = playCords(sheet)
