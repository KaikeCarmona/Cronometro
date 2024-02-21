from tkinter import *;
import tkinter;   
 
color1 = "#0a0a0a"; # black / preta
color2 = "#fafcff"; # white / branca
 
#configurando a janela ---------

window = Tk(); 
window.title("Time to sleep"); #titulo da janela
window.geometry('300x180'); #tamanho da janela
window.configure(bg=color1); #cor de fundo 
window.resizable(width=FALSE, height=FALSE); #não permite que o tamanho da janela seja alterado

#definindo variaveis globais
global time, rotate, counter, limiter;

time = "00:00:00";
rotate =  FALSE;
counter = 0;
limiter = 59;

#função para dar inicio a funcao start
def start_true():
    global rotate
    if not rotate:  # Verifica se o cronômetro não está em execução
        rotate = True
        start()
    else:
        print("O cronômetro já está em execução!")
    

#função para iniciar
def start():
    global time, counter, limiter

    if rotate:
        if counter:


            #Rodando o cronometro
            label_time['font'] = 'Arial 50 bold'
            temporary = time;
            h,m,s = map(int, temporary.split(":")); 
            
            #passando os valores para inteiro para fazer a logica do timer
            h = int(h);
            m = int(m);
            s = int(counter)
        
            if(s>=limiter):
                 counter = 0
                 m += 1;
                 s += counter
                 if(m>=limiter):
                    h += 1;

            s = str(0)+str(s)
            m = str(0)+str(m)
            h = str(0)+str(h)

            #atualizando os valores a cada vez que um numero é alterado
            temporary = str(h[-2:])+":"+ str(m[-2:]) + ":" + str(s[-2:]);
            label_time['text'] = temporary;
            time = temporary;
        

        label_time.after(1000, start) #a cada um segundo, a função start é chamada para fazer a alteração do valor da label time
        counter += 1;
     

def pouse():
    global rotate;
    rotate = False;
    

def restart():
    global time, counter;
    counter = 0
    time = "00:00:00";
    label_time['text'] = time;
 




#criando labels ---------
label_time = Label(window, text=time, fon=('Arial 50 bold'), bg=color1, fg=color2); #label para o titulo do timer, passando o nome, fonte, e cores de fundo e da fonte
label_time.place(x=14, y=25) # passando a posição da label dentro da janela


#criando botões ---------
button_start = Button(window, command=start_true, text="Start", width=10, height=2, bg=color1, fg=color2, font=('ivy 8 bold'), relief='raised', overrelief='ridge');
button_start.place(x = 20, y= 110);

button_pouse = Button(window,command=pouse, text="Pause", width=10, height=2, bg=color1, fg=color2, font=('ivy 8 bold'), relief='raised', overrelief='ridge');
button_pouse.place(x = 110, y= 110);

button_restart = Button(window,command=restart, text="Restart", width=10, height=2, bg=color1, fg=color2, font=('ivy 8 bold'), relief='raised', overrelief='ridge');
button_restart.place(x = 200, y= 110);

window.mainloop();




    
