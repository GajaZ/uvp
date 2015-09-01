from tkinter import*
import random

#barva cifer na ruleti
rdeca = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
crna = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
zelena = [0]


class Stevec():
    def __init__(self, master):

        menu = Menu(master)
        master.config(menu = menu)

        file_menu = Menu(menu)
        menu.add_cascade(label="File", menu = file_menu)
        file_menu.add_command(label="Save",command = self.shrani)
        file_menu.add_separator()
        file_menu.add_command(label="Quit", command = master.destroy)
       
        frame = Frame(master)
        frame.pack()


        self.stevec = 100
        self.stava = 0

        self.counter_c = 0
        self.counter_r = 0
        self.counter_s = 0
        self.counter_l = 0
        self.counter_zero = 0

        self.zeton = 0
        self.stevilo_iger = 0

    
 #stavimo lahko na crno, rdečo, sodo in liho cifro ter na 0
        
        def klik_c():            
            self.counter_c += self.zeton
            gumb_crna.config(text = self.counter_c)
            self.stevec -= self.zeton
            self.napis_stevec.set(str(self.stevec))
            self.stava += self.zeton
            self.napis_stava.set(str(self.stava))

        def klik_r():
            self.counter_r +=self.zeton
            gumb_rdeca.config(text = self.counter_r)
            self.stevec -= self.zeton
            self.napis_stevec.set(str(self.stevec))
            self.stava += self.zeton
            self.napis_stava.set(str(self.stava))
            
        def klik_s():
            self.counter_s +=self.zeton
            gumb_sodo.config(text = self.counter_s)
            self.stevec -= self.zeton
            self.napis_stevec.set(str(self.stevec))
            self.stava += self.zeton
            self.napis_stava.set(str(self.stava))

        def klik_l():
            self.counter_l += self.zeton
            gumb_liho.config(text = self.counter_l)
            self.stevec -= self.zeton
            self.napis_stevec.set(str(self.stevec))
            self.stava += self.zeton
            self.napis_stava.set(str(self.stava))

        def klik_zero():
            self.counter_zero += self.zeton
            gumb_zero.config(text = self.counter_zero)
            self.stevec -= self.zeton
            self.napis_stevec.set(str(self.stevec))
            self.stava += self.zeton
            self.napis_stava.set(str(self.stava))
            

 #iziramo lahko med žetoni s katerimi bomo stavili
            
        def zeton_2():
            self.napis_zgoraj.set("Izbrali ste žeton za 2€. Položite stavo!")
            self.zeton = 2

        def zeton_5():
            self.napis_zgoraj.set("Izbrali ste žeton za 5€. Položite stavo!")
            self.zeton = 5

        def zeton_10():
            self.napis_zgoraj.set("Izbrali ste žeton za 10€. Položite stavo!")
            self.zeton = 10
            
 #položili smo stave in igra se lahko začne!
            
        def zacni():
            self.stevilo_iger += 1
            print(self.stevec)
            print(self.counter_c, self.counter_r, self.counter_l, self.counter_s, self.counter_zero)

                        
            if self.counter_c != 0 or self.counter_r != 0 or self.counter_s != 0 or self.counter_l != 0 or self.counter_zero != 0:
                number = random.randrange (0,37)
                color = ""
                if number in rdeca:
                    print (number, "rdeča")
                    color = "red"
                    if self.counter_r != 0:
                        self.stevec = self.stevec + self.counter_r * 1.5
                    elif number%2 == 0 and number != 0 and self.counter_s != 0:
                        self.stevec = self.stevec + self.counter_s * 1.5
                    elif number%2 != 0 and self.counter_l != 0:
                        self.stevec = self.stevec + self.counter_l * 1.5    
                    
                elif number in crna:
                    print (number, "črna")
                    color = "black"
                    if self.counter_c != 0:
                        self.stevec = self.stevec + self.counter_c * 1.5
                    elif number%2 == 0 and number != 0 and self.counter_s != 0:
                        self.stevec = self.stevec + self.counter_s * 1.5
                    elif number%2 != 0 and self.counter_l != 0:
                        self.stevec = self.stevec + self.counter_l * 1.5

                elif number in zelena:
                    print (number, "zelena")
                    color = "green"
                    if self.counter_zero != 0:
                        self.stevec = self.stevec + self.counter_zero * 1.5                        

                print("After:", self.stevec)

                self.label_zreb.configure(text=str(number), foreground = color)

                
                self.stava = 0
                self.counter_c = 0
                self.counter_s = 0
                self.counter_l = 0
                self.counter_r = 0
                self.counter_zero = 0
                gumb_liho.config(text = self.counter_l)
                gumb_sodo.config(text = self.counter_s)
                gumb_rdeca.config(text = self.counter_r)
                gumb_crna.config(text = self.counter_c)
                gumb_zero.config(text = self.counter_zero)
                
                
                self.napis_stava.set(str(self.stava))
                self.napis_stevec.set(str(self.stevec))
                

            else:
                self.napis_zgoraj.set("MINIMALNA STAVA ZNAŠA 2€!")
                
                
                
 #različni gumbi na katere lahko pritiskamo
                
        gumb_crna = Button(frame, text=self.counter_c, command=klik_c)
        gumb_crna.grid(row=3, column=4)

        gumb_rdeca = Button(frame, text=self.counter_r, command = klik_r)
        gumb_rdeca.grid(row=3, column=7)
    
        gumb_sodo = Button(frame, text=self.counter_s, command = klik_s)
        gumb_sodo.grid(row=4, column=4)

        gumb_liho = Button(frame, text=self.counter_l, command = klik_l)
        gumb_liho.grid(row=4, column=7)

        gumb_zero = Button(frame, text=self.counter_zero, command = klik_zero)
        gumb_zero.grid(row=5, column=4)

        gumb_zacni = Button(frame, text="ZAČNI!", command = zacni)
        gumb_zacni.grid(row=1, column=5)

        gumb_2e = Button(frame, text="2€", command = zeton_2)
        gumb_2e.grid(row=3, column=10)

        gumb_5e = Button(frame, text="5€", command = zeton_5)
        gumb_5e.grid(row=4, column=10)

        gumb_10e = Button(frame, text="10€", command = zeton_10)
        gumb_10e.grid(row=5, column=10)
        
 #različni napisi, ki naredijo igro bolj razumljivo za igralca
        
        self.napis_stevec = StringVar(value=str(self.stevec))
        label_stevec = Label(frame, textvariable=self.napis_stevec)
        label_stevec.grid(row=2, column=10)

        self.napis_stava = StringVar(value=str(self.stava))
        label_stava = Label(frame, textvariable=self.napis_stava)
        label_stava.grid(row=6, column=6)

        self.napis_zgoraj = StringVar(value="Izberi vrednost žetona!")
        napis = Label(frame, textvariable = self.napis_zgoraj)
        napis.grid(row=2, column=3, columnspan=4)

        self.label_zreb = Label(frame, text="", fg="red")
        self.label_zreb.grid(row=1, column=8)

        self.napis_zreb=Label(frame, text = "Izbrana je številka ")
        self.napis_zreb.grid(row=1, column=7)

        self.label_stanje = Label(frame, text="STANJE:")
        self.label_stanje.grid(row=2, column=9)

        self.label_evri = Label(frame, text="€")
        self.label_evri.grid(row=2, column=11)

        self.label_stava = Label(frame, text="Stavili ste")
        self.label_stava.grid(row=6, column=5)

        self.label_evri1 = Label(frame, text="€")
        self.label_evri1.grid(row=6, column=7)

        self.label_crna = Label(frame, text="ČRNA:")
        self.label_crna.grid(row=3, column=3)

        self.label_rdeca = Label(frame, text="RDEČA:")
        self.label_rdeca.grid(row=3, column=6)

        self.label_sodo = Label(frame, text="SODO:")
        self.label_sodo.grid(row=4, column=3)

        self.label_liho = Label(frame, text="LIHO:")
        self.label_liho.grid(row=4, column=6)

        self.label_zero = Label(frame, text="NULA:")
        self.label_zero.grid(row=5, column=3)

        napisIgralec = Label(frame, text="Igralec:").grid(row=0, column=0)
        self.Igralec = StringVar(frame)
        polje_Igralec = Entry(frame, textvariable = self.Igralec)
        polje_Igralec.grid(row=0, column=1)
        
 # funkcija, ki shrani naše finančne vzpone in padce
    def shrani(self, *args):
        with open("moje_finance.txt", "at") as f:
            print("{0}: vaše končno stanje po {1} igrah znaša {2}€".format(self.Igralec.get(), self.stevilo_iger, self.stevec), file=f)



root = Tk()

aplikacija = Stevec(root)

root.mainloop()
