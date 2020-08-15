import pyautogui,time
time.sleep(4)
f = open('vanessa.txt','r')

for word in f:
    pyautogui.typewrite(word)
    pyautogui.press('enter')