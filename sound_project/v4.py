from pynput import keyboard
import time

def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(
            key.char))
        if key.char == 'b':
            print("what")
            global beats
            beats.append(time.time())
        else:
            pass
            
    except AttributeError:
        print('special key {0} pressed'.format(
            key))

def on_release(key):
    print('{0} released'.format(
        key))
    if key == keyboard.Key.shift:

        # Stop listener
        return False


##MAIN
start = time.time()
beats = []
play = True
listener = keyboard.Listener(on_press=on_press,on_release=on_release)
listener.start()


listener.join()

try:
    b = beats[0]
    for i in range(len(beats)):
        beats[i] = beats[i]-b
except:
    pass
end = time.time()
print(end - start, beats)
