from tkinter import * 
root = Tk()
root.title("Quản lý sinh viên")
root.minsize(height=500,width=500)
Label(root, text= "Ưng dụng quản lý sinh viên ", fg='red', font=('cambria', 16), width=20).grid(row=0)
Listbox(root, width=80, height=20).grid(row=1, columnspan=2)
Label(root, text= "Ưng dụng quản lý sinh viên ", fg='red', font=('cambria', 16), width=20).grid(row=0)
root.mainloop()