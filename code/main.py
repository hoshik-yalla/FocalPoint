import functions.miniplayer as mp
import functions.HID as hid
import functions.window as window
import time


def FocusSession(hwnd, duration,threshold):
     print("\n\nSession Started")
     print(f"Target HWND: {hwnd}")
     print(f"Duration: {duration}")
     print(f"Idle Threshold: {threshold}")
     mp.initialize()
      


print("Welcome to FocalPoint v1")
print("Loading...")
print("\n")
time.sleep(3)

#Selecting target window
print("Choose the appilcation's window for today's session (Only 1 Window Supported)")
toutput,houtput = window.run()
for i in toutput:
    print("["+str(toutput.index(i))+"] "+i)
wind = int(input("\nType the index no. of the window: "))
while not (wind >= 0 and wind < len(toutput)):
     print("Invalid index")
     wind = int(input("\nType the index no. of the window: "))

#Duration input - converts to seconds
dur = int(input("\nInput the duration in minutes: "))
dur *= 60
thres = int(input("\nInput the inactivity threshold in minutes: "))
thres *= 60

FocusSession(houtput[wind], dur, thres)