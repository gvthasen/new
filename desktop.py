from tkinter import *
 main = Tk()
 desktop.title("STC")
 main.title("STC")

 main.geometry("200x200)

  main.configure(background='violet')

 Label(main, text="username", font=40, fg="blue", bg="red").grid(row=1, column=1)

Label(main.text = "password", font = 40, fg = "green", bg = "black").grid(row=2, column=1)


 Label(main, text="password", font=40, fg="green", bg="black").grid(row=2, column=1)

 Label(main, text="password", font=40, fg="orange", bg="purple").grid(row=2, column=1)

 text1 = Entry(main, width=20, bg="white")

 text1.grid(row=1, column=2)

 text2 = Entry(main, width=20, bg="white")

 text2.grid(row=2, column=2)

 main.configure(background='purple')
e = Button(main, width=10, text="submit", bg="black", fg="white", font=20, command=show)

e = Button(main, width=10, text="submit", bg="black", fg="white", font=20, command=show)


 e = Button(main, width=10, text="submit", bg="black", fg="white", font=20)

 e.grid(row=5, column=3)

 e.grid(row=5, column=2)

