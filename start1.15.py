import tkinter as tk
from tkinter import Frame, Button, Label, PhotoImage
from random import choice
import webbrowser

# nice font for application
global global_font
global_font = 'Verdana 12'

counter, hits, accuracy = 0, 0, 0

def count_p():
    global counter, hits, accuracy
    counter += 1    
    hits += 1
    accuracy = round(((100 / counter) * hits),2)
    l4.config(text=counter)
    l6.config(text=str(accuracy)+' %')

def count():
    global counter, hits, accuracy
    counter += 1
    hits += 0
    try:
        accuracy = round(((100 / counter) * hits),2)
    except:
        ZeroDivisionError('0')
    l4.config(text=counter)
    l6.config(text=str(accuracy)+' %')

def toplevel1():
    top=tk.Toplevel()
    top.geometry("600x300+300+250")
    top.overrideredirect(1)
    top.configure(bg='lightblue')

    def check(letter):
        if word_print[1] == letter:
            button_check.config(bg='green')            
            count_p()
        else:
            button_check.config(bg='red')
            count()
        button_check.after(1500, lambda: button_check.config(bg='lightgray'))
        top.after(1650, lambda: top.destroy())

    b1 = tk.Button(top, state=tk.DISABLED, command=lambda: check(letter='ch'))
    b2 = tk.Button(top, state=tk.DISABLED, command=lambda: check(letter='h'))
    b3 = tk.Button(top, state=tk.DISABLED, command=lambda: check(letter='rz'))
    b4 = tk.Button(top, state=tk.DISABLED, command=lambda: check(letter='ż'))
    b5 = tk.Button(top, state=tk.DISABLED, command=lambda: check(letter='ó'))
    b6 = tk.Button(top, state=tk.DISABLED, command=lambda: check(letter='u'))

    def change1():
        b1['state'] = tk.NORMAL
        b2['state'] = tk.NORMAL

    def change2():
        b3['state'] = tk.NORMAL
        b4['state'] = tk.NORMAL

    def change3():
        b5['state'] = tk.NORMAL
        b6['state'] = tk.NORMAL

    def dict_word():
        with open("proste.txt", "r", encoding='iso-8859-2') as file:
            return(choice(file.readlines()).replace('\n', ''))

    def symbols():
        word = dict_word()
        if 'ch' in word:
            wordch = word.replace('ch', '_')
            change1()
            return(wordch, 'ch')
        elif 'h' in word:
            wordhh = word.replace('h', '_')
            change1()
            return(wordhh, 'h')
        elif 'rz' in word:
            wordrz = word.replace('rz', '_')
            change2()
            return(wordrz, 'rz')
        elif 'ż' in word:
            wordzz = word.replace('ż', '_')
            change2()
            return(wordzz, 'ż')
        elif 'ó' in word:
            wordou = word.replace('ó', '_')
            change3()
            return(wordou, 'ó')
        elif 'u' in word:
            worduu = word.replace('u', '_')
            change3()
            return(worduu, 'u')

    word_print = symbols()

    label = tk.Label(top, bg='lightblue').pack()

    label1 = tk.Label(top, bg='lightblue', relief='sunken', font=("Verdana", 36))
    label1.pack(pady='15')
    label1.config(text=word_print[0])

    image1 = PhotoImage(file='button_ch.png')
    image2 = PhotoImage(file='button_hh.png')
    image3 = PhotoImage(file='button_rz.png')
    image4 = PhotoImage(file='button_zz.png')
    image5 = PhotoImage(file='button_uo.png')
    image6 = PhotoImage(file='button_uu.png')

    b1.config (image = image1)
    b2.config (image = image2)
    b3.config (image = image3)
    b4.config (image = image4)
    b5.config (image = image5)
    b6.config (image = image6)

    b1.image = image1
    b2.image = image2
    b3.image = image3
    b4.image = image4
    b5.image = image5
    b6.image = image6

    b1.place(x='60' , y='90')
    b2.place(x='150', y='90')
    b3.place(x='226', y='90')
    b4.place(x='314', y='90')
    b5.place(x='388', y='90')
    b6.place(x='468', y='90')

    button_check = tk.Button(top, text='SPRAWDŹ', state=tk.DISABLED, font=((),20))
    button_check.place(x='236', y='220')

def toplevel2():
    top=tk.Toplevel()
    top.geometry("600x300+300+250")
    top.overrideredirect(1)
    top.configure(bg='lightblue')

    label = tk.Label(top, bg='lightblue', text='Program ten był tworzony podczas konkursu', font=("Verdana", 20))
    label.pack(pady='30')

    def dsp2017():
        webbrowser.open("http://devstyle.pl/daj-sie-poznac/")
        root.destroy()

    button = tk.Button(top, text='Quit', command=dsp2017)
    image = PhotoImage(file='dsp2017-1.png')
    button.config (image = image)
    button.image = image
    button.place(x='6', y='100')

    button = tk.Button(top, text='Naciśnij, aby wrócić do okna głównego aplikacji.', command=top.destroy)
    button.place(x='150', y='260')
    
root = tk.Tk()
root.geometry("600x400+300+150")
root.title("Mistrz ortografii")
# applying font
root.option_add('*Font', global_font)
root.overrideredirect(1)

tf = tk.Frame(root, height='100' ,width='600').pack(side='top')
bf = tk.Frame(root, height='300', width='600', bg='lightblue').pack(side='bottom')

b1 = tk.Button(tf, bg='yellow', text='Wylosuj słowo', command=toplevel1)
b1.place(height='100' ,width='200', x='0', y='0')
b2 = tk.Button(tf, bg='orange', text='O programie', command=toplevel2)
b2.place(height='100' ,width='200', x='200', y='0')
b3 = tk.Button(tf, bg='red', text='Wyjście', command=root.destroy)
b3.place(height='100' ,width='200', x='400', y='0')

l1 = tk.Label(bf, bg='lightblue', text='Wylosuj słowo i sprawdź \nczy wiesz, jak się je pisze.', font=(("Verdana"),20))
l1.place(x='180', y='140')

l2 = tk.Label(bf, bg='lightblue', text='I zostań Mistrzem Ortografii.', font=(("Verdana"),20))
l2.place(x='166', y='290')

l3 = tk.Label(bf, bg='lightblue', text='Ilość wylosowanych słów: ', font=global_font)
l3.place(x='20', y='360')

l4 = tk.Label(bf, bg='lightblue', text=counter)
l4.place(x='180', y='360')

l5 = tk.Label(bf, bg='lightblue', text='Twoja skuteczność: ', font=global_font)
l5.place(x='20', y='380')

l6 = tk.Label(bf, bg='lightblue', text=accuracy)
l6.place(x='180', y='380')
                  
root.mainloop()
