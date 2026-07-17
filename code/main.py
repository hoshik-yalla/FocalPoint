import functions.miniplayer as mp
import functions.HID as hid
import functions.window as window
import threading
import time


def FocusSession(hwnd, duration,threshold):
     print(f"Target HWND: {hwnd}")
     print(f"Duration: {duration}")
     print(f"Idle Threshold: {threshold}")

     #placeholder variables
     elapsed = 0
     dead = False
     window_focus = False
     hid_activity = False
     threshold_hit = None
     health = 100
     #Mainframe loop
     print("Session started")
     while elapsed < duration:
          hid_activity = hid.mouse_activity() or hid.key_activity()
          window_focus = window.get_focus(hwnd)
          elapsed += 10

          #target window + activity
          if hid_activity and window_focus:
               health += 10
               if health > 100:
                    health = 100
               if threshold_hit != None:
                    threshold_hit = None
          #wrong window + activity
          if (not window_focus) and hid_activity:
               health -= 10
               if health < 0:
                    health = 0
                    dead = True
          #no activity
          if not hid_activity:
               health -= 2
               if health < 0:
                    health = 0
                    dead = True
               threshold_hit = elapsed
          
          #threshold hit
          if threshold_hit != None:
               if elapsed - threshold_hit >= threshold:
                    health -= 30
                    if health < 0:
                         health = 0
                         dead = True
          
          #send updated health
          print(mp.update_activity(health))

     #Post session/dead logic
     if not dead:
          print("Focus Session Finish")
          mp.survived()
     else:
          print("Campfire died :(")


print("Welcome to FocalPoint v1")
print("Loading...")
print("\n")
time.sleep(3)

#Selecting target window
print("Choose the appilcation's window for today's session (Only 1 Window Supported)")
toutput,houtput = window.menu()
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

mp.initialize(lambda: threading.Thread(
     target=FocusSession,
     args=(houtput[wind], dur, thres),
     daemon=True,
).start())