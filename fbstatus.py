#importing necessary modules
import pyautogui, time

#time for adjustments
time.sleep(1)

pyautogui.click(1253,20)
pyautogui.sleep(2)

#opening status file
f=open("status",'r')

#for opening chrome from desktop
pyautogui.click(50,763)
pyautogui.sleep(1)
pyautogui.typewrite('chrome')
pyautogui.press('enter')
pyautogui.sleep(2)

#for searching fb
pyautogui.click(434,40)
pyautogui.sleep(1)

#for typing url
pyautogui.typewrite('www.facebook.com')
pyautogui.press('enter')
pyautogui.sleep(3)

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

#closing the chrome
pyautogui.click(1350,20)





