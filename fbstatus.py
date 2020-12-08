#importing necessary modules
import pyautogui, time

#time for adjustments
time.sleep(5)

#opening status file
f=open("status",'r')

#clicking on reqd coordinates
pyautogui.click(520,420)

#sleeping to compromise slow internet
pyautogui.sleep(1)

#clicking on reqd coordinates
pyautogui.click(480,320)


#typing the status
for word in f:
    pyautogui.typewrite(word)

#posting the status
pyautogui.click(590,580)

changed




