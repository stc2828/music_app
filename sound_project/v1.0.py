import playCords
from pynput import keyboard
import time

class main:
    beats = []
    def __init__(self):
        #self.takeBeats()
        pass

    def takeBeats(self):
        start = time.time()
        #global beats
        def on_press(key):
            try:
                if key.char == 'b':
                    #global beats
                    self.beats.append(time.time())
                if key.char == 'm':
                    return False
                else:
                    pass
                    
            except AttributeError:
                print('special key {0} pressed'.format(key))

        def on_release(key):
            #print('{0} released'.format(key))
            if key == keyboard.Key.shift:
                return False

        listener = keyboard.Listener(on_press=on_press,on_release=on_release)
        listener.start()
        listener.join()

        try:
            begin = self.beats[0]
            for i in range(len(self.beats)):
                self.beats[i] = self.beats[i]-begin
        except:
            pass
        end = time.time()
        print("original beats:")
        print(end - start, self.beats)
        #return beats


    def interpretBeats(self):
        beats = self.beats
        print (beats)
        beats2 = []
        diff = []
        a = 0
        if len(beats)%2 == 1:
            a - 1
            l += 1
        else:
            l = int(len(beats)/2)
            middle = beats[l]
            i = 0
            while i < l-1-a:
                diff += [(beats[i+1]-beats[i] - beats[i+1+l]+beats[i+l])]
                beats2 += [(beats[i+1]-beats[i] + beats[i+1+l]-beats[i+l])/2]
                i += 1
            beats2 += [beats[l]-beats[l-1]]
        print("normalized beats:")
        print(beats2)
        print("difference:")
        print(diff)
        diff2 = [diff[i]/beats2[i] for i in range(len(diff))]

        return self.play(beats2)

    def play(self, beats):
        sheet = []
        start, end = 0, 0
        for i in beats:
            
            sheet.append([[440], i/2, start])
            start += i

        return sheet

if __name__ == '__main__':
    #beats = []

    a = main()
    #a.beats = [1578723944.200133, 1578723944.740795, 1578723945.017806, 1578723945.336797, 1578723945.874872, 1578723946.150868, 1578723946.466731, 1578723947.02177, 1578723947.374717, 1578723947.697716, 1578723948.849678, 1578723949.1788769, 1578723949.470699, 1578723949.776474, 1578723950.0804212, 1578723950.388936, 1578723951.000643, 1578723951.188752, 1578723953.0236568, 1578723953.40685, 1578723953.708606, 1578723953.989654, 1578723954.456775, 1578723954.794497, 1578723955.100502, 1578723955.56839, 1578723955.884396, 1578723956.179636, 1578723957.336579, 1578723957.64626, 1578723957.922476, 1578723958.191524, 1578723958.4775481, 1578723958.7530859, 1578723959.317467]
    #begin = a.beats[0]
    #for i in range(len(a.beats)):
        #a.beats[i] = a.beats[i]-begin
    #print(a.beats)
    a.takeBeats()
    sheet = a.interpretBeats()
    playCords.playCords(sheet)
    
    
