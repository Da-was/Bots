import pyautogui,time
#aviso,santana e vanessa
braba = input('qual vai ser a braba?')
f = open(braba + '.txt','r')
time.sleep(4)
for word in f:
    pyautogui.typewrite(word)
    pyautogui.press('enter')