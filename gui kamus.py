from tkinter import*
from tkinter import messagebox

main_window = Tk()
main_window.title('kamus bahasa')
main_window.geometry('350x400')

class klik:

    def __init__(self, master):
    
        frame = Frame(main_window, width=400, height=300)
        frame.pack()

        self.button1 = Button(frame, text="indonesia-inggris")
        self.button1.grid(row=6, column=0)

        self.button2 = Button(frame, text="inggris-indonesia")
        self.button2.grid(row=6, column=1)

        self.label = Label(frame, text="masukkan bahasa")
        self.label.grid(row=2, column=0, sticky="w")

        self.entry = Entry(frame)
        self.entry.grid(row=2, column=1)

        self.checkbutton = Checkbutton(frame, text="saya bukan robot")
        self.checkbutton.grid(row=3)


    def action():
        buah=input("Masukkan kata yang dicari : ")
        for i in range(len(x)):
            if buah in x:
                print("<indonesia : inggris>")
                print(buah,":",x[buah])
            else:
                print("tidak ada")

        i=input("Apakah anda ingin melanjutkan?(y/t)")
        if i == "y":
            return kamus(x)
        elif i == "t":
            print("SELAMAT TINGGAL!!!")
            
o =  klik(main_window)           
main_window.mainloop()