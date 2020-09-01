import pyautogui,time
import textos
#aviso,cirilo,pneu, santana e vanessa
braba = input('qual vai ser a braba?')
f = open('textos/'+braba + '.txt','r')
time.sleep(4)
for word in f:
    pyautogui.typewrite(word)
    pyautogui.press('enter')
print('terminei a braba')