from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import mysql.connector
from tkinter import messagebox
class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("STUDENT MANAGEMENT SYSTEM")

        #variable
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_std_id = StringVar()
        self.var_std_name = StringVar()
        self.var_div = StringVar()
        self.var_gender = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_email = StringVar()
        self.var_teacher = StringVar()


        #1st
        img = Image.open(r"college_images\7th.jpg")
        img = img.resize((540,160), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        self.btn_1 = Button(self.root, image=self.photoimg, cursor="hand2")
        self.btn_1.place(x=0,y=0,width=510,height=160)

        #2st
        img_2 = Image.open(r"college_images\6th.jpg")
        img_2 = img_2.resize((540,160), Image.ANTIALIAS)
        self.photoimg_2 = ImageTk.PhotoImage(img_2)

        self.btn_1 = Button(self.root, image=self.photoimg_2, cursor="hand2")
        self.btn_1.place(x=540,y=0,width=510,height=160)

        #1st
        img_5 = Image.open(r"college_images\5th.jpg")
        img_5 = img_5.resize((540,160), Image.ANTIALIAS)
        self.photoimg_3 = ImageTk.PhotoImage(img_5)

        self.btn_1 = Button(self.root, image=self.photoimg_3, cursor="hand2")
        self.btn_1.place(x=1000,y=0,width=510,height=160)

        #bg

        img_4 = Image.open(r"college_images\university.jpg")
        img_4 = img_4.resize((1530,710), Image.ANTIALIAS)
        self.photoimg_4 = ImageTk.PhotoImage(img_4)

        bg_lbl = Label(self.root, image=self.photoimg_4, bd=2, relief=RIDGE)
        bg_lbl.place(x=0,y=160,width=1530,height=710)
        
        lbl_title = Label(bg_lbl, text="STUDENT MANAGEMENT SYSTEM", font=("times new roman",37,"bold"), fg = "blue", bg="white")
        lbl_title.place(x=0,y=0, width=1530, height=50)
        # manage frame
        Mange_frame = Frame(bg_lbl, bd = 2, relief=RIDGE, bg="white")
        Mange_frame.place(x=15,y=55, width=1500,height=800)

        #left frame 
        DataLeft = LabelFrame(Mange_frame,bd=4, relief=RIDGE,padx=2, text="STUDENT INFORMATION ", font=("times new roman",12,"bold"), fg = "red", bg="white")
        DataLeft.place(x=10,y=10, width=660, height=540)

        #img
        img_5 = Image.open(r"college_images\3rd.jpg")
        img_5 = img_5.resize((650,120), Image.ANTIALIAS)
        self.photoimg_5 = ImageTk.PhotoImage(img_5)

        my_img = Label(DataLeft, image=self.photoimg_5, bd=2, relief=RIDGE)
        my_img.place(x=0,y=0,width=650,height=120)

        # Current course LabelFrame Information
        std_lbl_info_frame = LabelFrame(DataLeft, bd=4, relief=RIDGE, padx=2, text="Current Course Information", font=("times new roman",12,"bold"), fg = "red", bg="white")
        std_lbl_info_frame.place(x=0,y=120,width=650, height=115)
        
        

        # department
        lbl_dep = Label(std_lbl_info_frame,text="Department", font=("arial",12,"bold"), bg="white")
        lbl_dep.grid(row=0, column=0, padx=2,sticky=W)

        combo_dep = ttk.Combobox(std_lbl_info_frame, textvariable=self.var_dep, font=("arial",12,"bold"), width=17, state="readonly")
        combo_dep["value"] = ("Select Department", "Computer", "IT","Civil")
        combo_dep.current(0)
        combo_dep.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        # course
        lbl_dep = Label(std_lbl_info_frame,text="Courses:", font=("arial",12,"bold"), bg="white")
        lbl_dep.grid(row=0, column=2, padx=2,sticky=W)

        combo_txt = ttk.Combobox(std_lbl_info_frame, textvariable=self.var_course, font=("arial",12,"bold"), width=17, state="readonly")
        combo_txt["value"] = ("Select Course", "FE", "SE","BE")
        combo_txt.current(0)
        combo_txt.grid(row=0, column=3, padx=2, pady=10, sticky=W)

        # YEAR
        lbl_dep = Label(std_lbl_info_frame,text="Year:", font=("arial",12,"bold"), bg="white")
        lbl_dep.grid(row=1, column=0, padx=2,sticky=W)

        combo_year = ttk.Combobox(std_lbl_info_frame,textvariable=self.var_year, font=("arial",12,"bold"), width=17, state="readonly")
        combo_year["value"] = ("Select Year", "2022-2023", "2023-2024","2024-2025")
        combo_year.current(0)
        combo_year.grid(row=1, column=1, padx=2, pady=10, sticky=W)

        # SEMESTER
        lbl_dep = Label(std_lbl_info_frame,text="Semester:", font=("arial",12,"bold"), bg="white")
        lbl_dep.grid(row=1, column=2, padx=2,sticky=W)

        combo_semester = ttk.Combobox(std_lbl_info_frame,textvariable=self.var_semester, font=("arial",12,"bold"), width=17, state="readonly")
        combo_semester["value"] = ("Select Semester", "Semster-1", "Semester-2")
        combo_semester.current(0)
        combo_semester.grid(row=1, column=3, padx=2, pady=10, sticky=W)

       
       # Class course LabelFrame Information
        std_lbl_class_frame = LabelFrame(DataLeft, bd=4, relief=RIDGE, padx=2, text="Class Course Information", font=("times new roman",12,"bold"), fg = "red", bg="white")
        std_lbl_class_frame.place(x=0,y=235,width=650, height=250)

        #ID
        lbl_id = Label(std_lbl_class_frame, font=("arial",12,"bold"),text="Student ID:", bg="white")
        lbl_id.grid(row=0, column=0,sticky=W,padx=2,pady=7)

        id_entry = ttk.Entry(std_lbl_class_frame,textvariable=self.var_std_id, font=("arial",12,"bold"),width=20)
        id_entry.grid(row=0,column=1,sticky=W,padx=2,pady=7)

        #Name
        lbl_id = Label(std_lbl_class_frame, font=("arial",12,"bold"),text="Student Name:", bg="white")
        lbl_id.grid(row=0, column=2,sticky=W,padx=2,pady=7)

        id_entry = ttk.Entry(std_lbl_class_frame,textvariable=self.var_std_name, font=("arial",12,"bold"),width=20)
        id_entry.grid(row=0,column=3,sticky=W,padx=2,pady=7)


        #Class division
        lbl_id = Label(std_lbl_class_frame, font=("arial",12,"bold"),text="Class devision:", bg="white")
        lbl_id.grid(row=1, column=0,sticky=W,padx=2,pady=7)

        id_entry = ttk.Combobox(std_lbl_class_frame,textvariable=self.var_div, font=("arial",12,"bold"),width=18)
        id_entry["value"] = ("Select","A", "B","C")
        id_entry.current(0)
        id_entry.grid(row=1,column=1,sticky=W,padx=2,pady=7)


        #Phone
        lbl_id = Label(std_lbl_class_frame, font=("arial",12,"bold"),text="Phone number:", bg="white")
        lbl_id.grid(row=1, column=2,sticky=W,padx=2,pady=7)

        id_entry = ttk.Entry(std_lbl_class_frame,textvariable=self.var_phone, font=("arial",12,"bold"),width=20)
        id_entry.grid(row=1,column=3,sticky=W,padx=2,pady=7)



        #Gender
        lbl_id = Label(std_lbl_class_frame, font=("arial",12,"bold"),text="Gender:", bg="white")
        lbl_id.grid(row=2, column=0,sticky=W,padx=2,pady=7)

        id_entry = ttk.Combobox(std_lbl_class_frame,textvariable=self.var_gender, font=("arial",12,"bold"),width=18)
        id_entry["value"] = ("Select gender","Male", "Feamle")
        id_entry.current(0)
        id_entry.grid(row=2,column=1,sticky=W,padx=2,pady=7)

         #Address
        lbl_id = Label(std_lbl_class_frame, font=("arial",12,"bold"),text="Address:", bg="white")
        lbl_id.grid(row=2, column=2,sticky=W,padx=2,pady=7)

        id_entry = ttk.Entry(std_lbl_class_frame,textvariable=self.var_address, font=("arial",12,"bold"),width=20)
        id_entry.grid(row=2,column=3,sticky=W,padx=2,pady=7)

         #Email
        lbl_id = Label(std_lbl_class_frame, font=("arial",12,"bold"),text="Email:", bg="white")
        lbl_id.grid(row=3, column=0,sticky=W,padx=2,pady=7)

        id_entry = ttk.Entry(std_lbl_class_frame,textvariable=self.var_email, font=("arial",12,"bold"),width=20)
        id_entry.grid(row=3,column=1,sticky=W,padx=2,pady=7)


         #Teacher name
        lbl_id = Label(std_lbl_class_frame, font=("arial",12,"bold"),text="Teacher name:", bg="white")
        lbl_id.grid(row=3, column=2,sticky=W,padx=2,pady=7)

        id_entry = ttk.Entry(std_lbl_class_frame,textvariable=self.var_teacher, font=("arial",12,"bold"),width=20)
        id_entry.grid(row=3,column=3,sticky=W,padx=2,pady=7)

        #Button Frame

        btn_frame = Frame(DataLeft,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=470,width=650,height=38)

        btn_Add = Button(btn_frame,text="Save",command=self.add_data,font=("arial",11,"bold"), width=17,bg="blue", fg="white")
        btn_Add.grid(row=0,column=0,padx=1)

        btn_update = Button(btn_frame,text="Update",command=self.update_data,font=("arial",11,"bold"), width=17,bg="blue", fg="white")
        btn_update.grid(row=0,column=1,padx=1)

        btn_delete = Button(btn_frame,text="Delete",command=self.delete_data,font=("arial",11,"bold"), width=17,bg="blue", fg="white")
        btn_delete.grid(row=0,column=2,padx=1)

        btn_reset = Button(btn_frame,text="Reset",command=self.reset_data,font=("arial",11,"bold"), width=17,bg="blue", fg="white")
        btn_reset.grid(row=0,column=3,padx=1)





        #right frame 
        DataRight = LabelFrame(Mange_frame,bd=4, relief=RIDGE,padx=2, text="STUDENT INFORMATION ", font=("times new roman",12,"bold"), fg = "red", bg="white")
        DataRight.place(x=680,y=10, width=800, height=540)

        #img1
        img_6 = Image.open(r"college_images\6th.jpg")
        img_6 = img_6.resize((780,200), Image.ANTIALIAS)
        self.photoimg_6 = ImageTk.PhotoImage(img_6)

        my_img= Label(DataRight, image=self.photoimg_6,bd=2,relief=RIDGE)
        my_img.place(x=0,y=0,width=790,height=200)
        
        #right frame 
        Search_Frame = LabelFrame(DataRight,bd=4, relief=RIDGE,padx=2, text="STUDENT INFORMATION ", font=("times new roman",12,"bold"), fg = "red", bg="white")
        Search_Frame.place(x=0,y=200, width=790, height=60)

        search_by = Label(Search_Frame, font=("arial",11,"bold"),text="Search by: ", fg="red",bg="white")
        search_by.grid(row=0,column=0,sticky=W,padx=5)


        #search
        self.var_com_search=StringVar()
        com_txt_search = ttk.Combobox(Search_Frame, state="readonly",textvariable=self.var_com_search,font=("arial",12,"bold"),width=18)
        com_txt_search['value'] = ("Select Option","Roll","Phone","StudentID")
        com_txt_search.current(0)
        com_txt_search.grid(row=0,column=1,sticky=W, padx=5)

        self.var_search = StringVar()
        txt_search = ttk.Entry(Search_Frame, textvariable=self.var_search,width=22,font=("arial",11,"bold"))
        txt_search.grid(row=0,column=2,padx=5)

        btn_search = Button(Search_Frame,text="Search",command=self.search_data,font=("arial",11,"bold"),width=14,bg="blue",fg="white")
        btn_search.grid(row=0,column=3,padx=5)

        btn_Showall = Button(Search_Frame,text="Show All",command=self.fetch_data,font=("arial",11,"bold"),width=14,bg="blue",fg="white")
        btn_Showall.grid(row=0,column=4,padx=5)

        # ========================Table and Scroll ================================

        table_frame = Frame(DataRight,bd=4,relief=RIDGE)
        table_frame.place(x=0,y=260,width=790,height=250)

        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)
        self.student_table = ttk.Treeview(table_frame, columns=("dep","course","year","semester","id","name","div","phone","address","email","teachername"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Department")
        
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("semester",text="Semester")
        self.student_table.heading("id",text="StudentID")
        self.student_table.heading("name",text="Student Name")
        self.student_table.heading("div",text="Class Div")
        self.student_table.heading("phone",text="Phone Number")
        self.student_table.heading("address",text="Student address")
        self.student_table.heading("teachername",text="Teacher Name")
        self.student_table.heading("email",text="Email")

        self.student_table["show"] = "headings"

        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("semester",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teachername",width=100)
        self.student_table.column("email",width=100)
        

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

    def add_data(self):
        if (self.var_dep.get() == "" or self.var_email.get() == "" or self.var_std_id.get() == ""):
            messagebox.showerror("Error", "All fields are required")
        else:
            try:
                conn = mysql.connector.connect(host="localhost",username="root",password="Duongcuong2141", database="qlsv")
                my_cusur = conn.cursor()
                my_cusur.execute("Insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_std_id.get(),
                    self.var_std_name.get(),
                    self.var_div.get(),
                    self.var_gender.get(),
                    self.var_email.get(),
                    self.var_phone.get(),  
                    self.var_address.get(), 
                    self.var_teacher.get() ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student has been added",parent = self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)

    #fecth
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost",username="root",password="Duongcuong2141", database="qlsv")
        my_cursur = conn.cursor()
        my_cursur.execute("select * from student")
        data = my_cursur.fetchall()
        if (len(data) != 0):
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    #get cursor
    def get_cursor(self, event=""):
        cursor_row = self.student_table.focus()
        content = self.student_table.item(cursor_row)
        data = content["values"]

        self.var_dep.set(data[0])
        self.var_course.set(data[1])
        self.var_year.set(data[2])
        self.var_semester.set(data[3])
        self.var_std_id.set(data[4])
        self.var_std_name.set(data[5])
        self.var_div.set(data[6])
        self.var_gender.set(data[7])
        self.var_email.set(data[8])
        self.var_phone.set(data[9])
        self.var_address.set(data[10])
        self.var_teacher.set(data[11])
    
    def update_data(self):
        if (self.var_dep.get() == "" or self.var_email.get() == "" or self.var_std_id.get() == ""):
            messagebox.showerror("Error", "All fields are required")
        else:
            try:
                update = messagebox.askyesno("Update","Are you sure update this student's data", parent=self.root)
                if update > 0:
                    conn = mysql.connector.connect(host="localhost",username="root",password="Duongcuong2141", database="qlsv")
                    my_cusur = conn.cursor()
                    my_cusur.execute("update student set Dep=%s,course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Gender=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s where StudentID=%s",(
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_std_name.get(),
                        self.var_div.get(),
                        self.var_gender.get(),
                        self.var_email.get(),
                        self.var_phone.get(),  
                        self.var_address.get(), 
                        self.var_teacher.get(),
                        self.var_std_id.get() ))
                else:
                    if not update:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student has been updated",parent = self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)

    #delete
    def delete_data(self):
        if (self.var_std_id.get() == "" ):
            messagebox.showerror("Error", "All fields are required")
        else:
            try:
                Delete = messagebox.askyesno("Delete","Are you want to delete this student")
                if Delete > 0:
                    conn = mysql.connector.connect(host="localhost",username="root",password="Duongcuong2141", database="qlsv")
                    my_cursur = conn.cursor()
                    sql = "delete from student where StudentID =%s"
                    value=(self.var_std_id.get(),)
                    my_cursur.execute(sql,value)
                else:
                    if not Delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Ypur data is deleted",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)

    #reset
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("")
        self.var_gender.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")

    #search
    def search_data(self):
        if self.var_com_search.get() == "" or self.var_search.get()=="":
            messagebox.showerror("Error", "Select options")
        else:
            try:
                conn = mysql.connector.connect(host="localhost",username="root",password="Duongcuong2141", database="qlsv")
                my_cusur = conn.cursor()
                my_cusur.execute("select * from student where "+str(self.var_com_search.get())+" LIKE '%"+str(self.var_search.get())+"%'")
                data = my_cusur.fetchall()
                if (len(data) != 0):
                    self.student_table.delete(*self.student_table.get_children())
                    for i in data:
                        self.student_table.insert("",END,values=i)
                    conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)

if __name__ == "__main__":
    root = Tk()
    OBJ = Student(root)
    root.mainloop()