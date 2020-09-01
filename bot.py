import pyautogui,time
from tkinter import*

root = Tk()
root.title("Spaming bot")

#-------------------------------functions------------------------------
def init_spam():

    braba = Select.get()
    Select.delete(0,END)

    f = open('textos/'+braba + '.txt','r')
    print(braba)
    time.sleep(4)
    for word in f:
        pyautogui.typewrite(word)
        pyautogui.press('enter')
    print('terminei a braba')
#-------------------------------Create side----------------------------

Frame = LabelFrame(root, text= "Como usar:", padx = 5, pady = 5 )
Frame2 = LabelFrame(root, text= "Definições:", padx = 5, pady = 5 ,)

Explain = Label(Frame,text = "Esse é um bot feito para espamar mensagens, tudo o que você precisa fazer \n"
+" é informar qual das mensagens você quer que seja espamada e clicar no \'iniciar\'.\n\n"
+"ALERTA : É aconselhado que você já esteja com o lugar que você quer espamar aberto, pois tera apenas \n"
+ " 5 segundos antes do spam acontecer após clicar em inicar.")



Select_text= Label(Frame2,text = "Insira o nome do arquivo de texto que você deseja espamar. ")
Select = Entry(Frame2)


Button_init = Button(Frame2, text = "Iniciar", fg = "red", padx = 30 ,command = init_spam)


#-------------------------------atatch side----------------------------
Explain.grid(row =0 , column = 0)

Select_text.grid(row = 0 , column = 0)
Select.grid(row =1 , column = 0)
Button_init.grid(row = 1, column = 1, columnspan = 2, padx = 63)

Frame.grid(row =0 , column = 0, padx = 10, pady = 10, sticky = W)
Frame2.grid(row =1 , column = 0, padx = 10, pady = 10, sticky = W)

root.mainloop()