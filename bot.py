import pyautogui,time, threading, os
from PIL import ImageTk, Image
from tkinter import*
from tkinter import messagebox




root = Tk()
root.title("Spaming bot")
root.geometry("+350+200")


TextsPath = "D:\\ViasualStudio\\Codigos\\botIdiota\\textos"

TexstList = os.listdir(TextsPath)



#-------------------------------functions------------------------------
def init_spam():

    global pode_spam 

    pode_spam = True

    try:
        braba = str(Selected.get())
        

        f = open('textos/'+braba,'r')
        print(braba)

        time.sleep(4)

        for word in f:
            if pode_spam == True:

                pyautogui.typewrite(word)
                pyautogui.press('enter')
            else :
                break

        print('terminei a braba')
        
        f.close()
        
    except FileNotFoundError:
        messagebox.showerror("Erro","Não foi possivel encontrar o arquivo \"" + braba + "\"!" )




def stop_spam():

    global pode_spam 
    pode_spam = False 


def first_spam():
    
    spam_t1 = threading.Thread(target= init_spam)
    spam_t1.start()
    
    

#-------------------------------Create side----------------------------

Frame = LabelFrame(root, text= "Como usar:", padx = 5, pady = 5 )
Frame2 = LabelFrame(root, text= "Definições:", padx = 5, pady = 5 ,)
Frame3 = LabelFrame(root, text= "Créditos:", padx = 5, pady = 5 ,)

Explain1 = Label(Frame,text = "Esse é um bot feito para espamar mensagens, tudo o que você precisa fazer \n"
+" é informar qual das mensagens você quer que seja espamada e clicar no \'iniciar\'.")

Explain2 = Label(Frame,text ="ALERTA : É aconselhado que você já esteja com o lugar que você quer espamar\n"
+ " aberto, pois tera apenas 5 segundos antes do spam acontecer após clicar em inicar.")

Explain3 = Label(Frame,text ="O botão \'Abortar\' serve para parar o bot antes que o documento de texto acabe.\n"
+"Ele fecha a janela do bot, então para poder abrir novamente é necessário reabrir o bot.")


Select_text= Label(Frame2,text = "Selecione o nome do arquivo de texto que você deseja espamar. ")
Selected = StringVar()
Select_Menu = OptionMenu(Frame2, Selected, *TexstList)
#Select = Entry(Frame2)
#Select.focus_set()

Button_init = Button(Frame2, text = "Iniciar", fg = "red", padx = 30 ,command = first_spam)
button_quit = Button(Frame2, text= "Abortar", padx = 30 , command = stop_spam, fg = "red")

status = Label(Frame3, text= "Criado por: João Laurindo", )

#-------------------------------atatch side----------------------------
Explain1.grid(row =0 , column = 0, padx = 80)
Explain2.grid(row =1 , column = 0)
Explain3.grid(row =2 , column = 0)

Select_text.grid(row = 0 , column = 0)
Select_Menu.grid(row =1 , column = 0)
Button_init.grid(row = 1, column = 1, padx = 9)
button_quit.grid(row = 1, column = 2, )

status.grid(row = 0 , column = 0)

Frame.grid(row =0 , column = 0, padx = 10, pady = 10, sticky = W+E)
Frame2.grid(row =1 , column = 0, padx = 10, pady = 10, sticky = W+E)
Frame3.grid(row =2 , column = 0, padx = 10, pady = 10, sticky = W+E)



root.mainloop()