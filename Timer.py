import threading
from tkinter import *
import os

color1 = "#0a0a0a"  # preta
color2 = "#fafcff"  # branca

# Configurando a janela principal
window = Tk()
window.title("Time to sleep")
window.geometry('300x180')
window.configure(bg=color1)
window.resizable(width=FALSE, height=FALSE)

# Variáveis globais
time = "00:00"
rotate = False
counter = 1
limiter = 60
s = 0
m = 0

# Função para iniciar o cronômetro
def start_true():
    global rotate, counter
    if not rotate:
        rotate = True
        start()
# Função para iniciar o cronômetro
def start():
    global time, counter, limiter, rotate

    if rotate:
        if counter <= 0:

            time = input_time.get()
            # Rodando o cronômetro
            label_time['font'] = 'Arial 50 bold'
            temporary = time
            m, s = map(int, temporary.split(":"))

            m = int(m)
            s += counter

            if s <= limiter:
                m += s // limiter
                s %= limiter
                if m <= limiter:
                    m %= limiter

            s = str(s).zfill(2)  # Garante que o segundo tenha dois dígitos
            m = str(m).zfill(2)  # Garante que o minuto tenha dois dígitos

            temporary = str(m[-2:]) + ":" + str(s[-2:])
            label_time['text'] = temporary
            time = temporary

            zerou(m, s)

        label_time.after(1000, start)
        counter -= 1

# Função chamada quando o tempo se esgota
def zerou(m, s):
    if m == "00" and s == "00":
        print("Zerou")
        show_confirmation_window()

        
# Função para pausar o cronômetro
def pause():
    global rotate
    rotate = False

# Função para reiniciar o cronômetro
def restart():
    global time, counter
    counter = 0
    time = "00:00"
    label_time['text'] = time
 
# Função para exibir a janela de confirmação
def show_confirmation_window():
    confirmation_window = Tk()
    confirmation_window.geometry('300x100')
    confirmation_window.configure(bg=color2)
    confirmation_window.resizable(width=FALSE, height=FALSE)

    # Função chamada ao clicar no botão "Sim"
    def yes_action():
        confirmation_window.destroy()
        pause()
        restart()

    # Função chamada ao clicar no botão "Não"
    def no_action():
        confirmation_window.destroy()
        window.destroy()

    # Função para desligar o PC caso o usuario não selecione nenhuma opção
    def desligar():
        os.system("shutdown -s -t 1") 

     # Label para exibir a questão
    label_confirmation_window = Label(confirmation_window, text="Ainda aind está ai?", font=('Arial 10 bold'), bg=color2, fg=color1)
    label_confirmation_window.pack(pady=10)

    # Criação dos botões
    yes_button = Button(confirmation_window, text="Sim", command=yes_action, width=10)
    no_button = Button(confirmation_window, text="Não", command=no_action, width=10)

    # Posicionamento dos botões
    yes_button.pack(side=LEFT, padx=20)
    no_button.pack(side=RIGHT, padx=20)

    confirmation_window.after(5000, desligar)  # Fecha a janela após 5 segundos

    confirmation_window.mainloop() # Executa a janela


# Entrada para definir o tempo
input_time = Entry(window, width=13, justify='center')
input_time.place(x=110, y=5)
input_time.insert(0, '00:01')

# Label para exibir o tempo
label_time = Label(window, text=time, font=('Arial 50 bold'), bg=color1, fg=color2)
label_time.place(x=60, y=25)

# Botões para iniciar, pausar e reiniciar
button_start = Button(window, command=start_true, text="Start", width=10, height=2, bg=color1, fg=color2,
font=('ivy 8 bold'), relief='raised', overrelief='ridge')
button_start.place(x=20, y=110)

button_pause = Button(window, command=pause, text="Pause", width=10, height=2, bg=color1, fg=color2,
font=('ivy 8 bold'), relief='raised', overrelief='ridge')
button_pause.place(x=110, y=110)

button_restart = Button(window, command=restart, text="Restart", width=10, height=2, bg=color1, fg=color2,
font=('ivy 8 bold'), relief='raised', overrelief='ridge')
button_restart.place(x=200, y=110)

# Iniciando a aplicação
window.mainloop()
