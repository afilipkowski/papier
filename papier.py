import random
import tkinter as tk

#wstepna konfiguracja okna programu
window = tk.Tk()
window.geometry("400x300")
window.title("Papier Kamien Nozyce")

#zmienne globalne przechowujace informacje o stanie gry
USER_SCORE = 0
COMP_SCORE = 0
USER_CHOICE = ""
COMP_CHOICE = ""

#funkcja zamieniajaca wybor na wartosc liczbowa
def choice_to_number(choice):
    pkn = {'kamien':0, 'papier':1, 'nozyce':2}
    return pkn[choice]

#funkcja przypisujaca wybor do podanej wartosci liczbowej
def number_to_choice(number):
    pkn = {0:'kamien', 1:'papier', 2:'nozyce'}
    return pkn[number]

#funkcja generujaca wybor komputera
def computer_choice():
    return random.choice(['papier', 'kamien', 'nozyce'])

#funkcja wybierajaca zwyciezce
def result(player_choice, cpu_choice):
    global USER_SCORE
    global COMP_SCORE
    player = choice_to_number(player_choice)
    cpu = choice_to_number(cpu_choice)
    if(player==cpu):
        print("Remis")
    elif((player-cpu)%3)==1:
        print("Wygrales")
        USER_SCORE+=1
    else:
        print("Przegrales")
        COMP_SCORE+=1
    text_area = tk.Text(master=window,height=12,width=30,bg="#FFFF99")
    text_area.grid(column=0,row=4)
    answer = "Twoj wybor: {uc} \n Wybor komputera: {cc} \nTwoj wynik: {u}\n Wynik komputera: {c}".format(uc=USER_CHOICE,cc=COMP_CHOICE,u=USER_SCORE,c=COMP_SCORE)
    text_area.insert(tk.END, answer)

def kamien():
    global USER_CHOICE
    global COMP_CHOICE
    USER_CHOICE ="kamien"
    COMP_CHOICE = computer_choice()
    result(USER_CHOICE, COMP_CHOICE)
def papier():
    global USER_CHOICE
    global COMP_CHOICE
    USER_CHOICE ="papier"
    COMP_CHOICE = computer_choice()
    result(USER_CHOICE, COMP_CHOICE)
def nozyce():
    global USER_CHOICE
    global COMP_CHOICE
    USER_CHOICE ="nozyce"
    COMP_CHOICE = computer_choice()
    result(USER_CHOICE, COMP_CHOICE)


button1 = tk.Button(text="       Kamien       ",bg="skyblue",command=kamien)
button1.grid(column=0, row=1)
button2 = tk.Button(text="       Papier      ",bg="pink",command=papier)
button2.grid(column=0,row=2)
button3 = tk.Button(text="      Nozyce     ",bg="lightgreen",command=nozyce)
button3.grid(column=0,row=3)

window.mainloop()




