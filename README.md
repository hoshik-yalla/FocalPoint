# FocalPoint
FocalPoint is an open-source Windows desktop application that encourages deep work by turning your focus into a survival game. Keep a virtual campfire alive by staying on task—lose focus, and the fire slowly dies.

## Why a campfire?
Unlike traditional Pomodoro timers, FocalPoint introduces consequences. Losing focus weakens the campfire, creating continuous feedback instead of simply counting down a timer.

**NOTE:** This app is only programmed and tested on Microsoft Windows 11, Python v3.11.9


## Usage

[Demo Video](https://youtu.be/ADfgo_LLXdI)

1. Clone the repo <br>
    ```
    git clone https://github.com/hoshik-yalla/FocalPoint.git
    ```

1. Install the necessary dependencies using the command below <br>
    ```
    cd FocalPoint
    ```
    ```
    pip install -r requirements.txt
    ```

2. Run main.py <br>
    ```
    python .\code\main.py
    ```

3. Follow instructions on the console
4. To exit the app - hover over the miniplayer and click on the X button to terminate the session.


## How does the app work
- The app updates the campfires health with a scoring system as illustrated below:

| Activity | Scoring |
| ----------- | ----------- |
| Window  focused + Mouse/Keyboard Activity | +10 HP / 10 sec |
| Window unfocused + Mouse/Keyboard Activity | -10 HP / 10 sec |
| No Mouse/Keyboard Activity | -2 HP / 10 sec |
| Idle threshold triggered | -30 HP / 10 sec|

<br>

- The idle threshold triggeres when you have no mouse/keyboard activity for more than x minutes <br> (you get to config the threshold before the session starts)

- The campfire gets weaker as you loose HP and it comes back to life as you start working again. 
If you hit 0 HP, the campfire dies and the session ends... no checkpoints, no progress bar, no timer.

- Under the hood: the application uses pyinput, keyboard and win32gui API to access HID activity and the windows active on the device. Primarily, pywebview is used to serve the campfire interface and handle communication between python and JS via its API class.

## Roadmap

- [x] Window selection
- [x] Campfire overlay
- [x] Health system
- [ ] Improved Active/Idle Filtering
- [ ] Improved error handling for invalid inputs
- [ ] MacOS/Linus Support
- [ ] Multi-window selection
- More coming soon...

## Want to contribute?
As a solo-programmer I might not have tested all the use cases this application contains, so feel free to contribute to the source code or opening an issue. I will try my best to review them and take action.

## AI Usage and declaration
ChatGPT was used for researching researching libraries and implementation approaches, dependencies, correcting typos/grammer in markdown files, and generating file trees to stay organized.

1. By case uses:
    - **Issue**: Pylance was operating with misconfigured python environment so any packages installed for this application wasn't being recognized.
    <br>
    Fix: Copilot access this workspace's settings file and fixed the issue.

    
    - **Issue**: Since pywebview's windows run on a loop based system, the code after the miniplayer wouldn't get executed. So I programmed it to run on a seperate thread. However, pywebview requires its windows to be run on the main thread.
    <br>
    Fix: Copilot moved the session logic into a secondary thread to reserver the main thread for pywebview. I specifically instructed it to avoid modifying the logic in any way or trying to "imrpove" the code.

    - Copilot was instructed to commit and push the repo as is and then proceed to program endpoints across the codebase to catch any potential bugs in the app. Once the tests are done. I would revert changes back to the latest commit and then start implementing the fixes.

Although AI was used in this project, I took necessary measures to ensure that the agent didn't contribute to the core logic and application flow.