import tkinter as tk

root = tk.Tk()

root.title('Pomodoro')
root.geometry('500x350')
root.minsize(width=250, height=120)

Uhr = tk.Label(master=root,
               font=('Arial', 45),
               fg='green',
               bg='black',
               width=20,
               height=4)
Uhr.pack(expand=True, fill='both')

root.mainloop()


def window(show_time):
    root = tk.Tk()
    root.title('Pomodoro')
    root.geometry('500x350')
    root.minsize(width=250, height=120)

    Uhr = tk.Label(master=root,
                   font=('Arial', 45),
                   fg='green',
                   bg='black',
                   width=20,
                   height=4)
    Uhr.pack(expand=True, fill='both')
    neuezeit = time.strftime('%H:%M:%S')
    if neuezeit != show_time:
        zeit = neuezeit
        Uhr.config(text=zeit)
    Uhr.after(200, window)
    root.mainloop()