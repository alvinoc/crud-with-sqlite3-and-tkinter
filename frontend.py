from tkinter import *
import backend

def get_selected_row(event):
    global selected_tuple
    index=list1.curselection()[0]
    selected_tuple=list1.get(index)
    entry1.delete(0,END)
    entry1.insert(END,selected_tuple[1])
    entry2.delete(0,END)
    entry2.insert(END,selected_tuple[2])
    entry3.delete(0,END)
    entry3.insert(END,selected_tuple[3])
    entry4.delete(0,END)
    entry4.insert(END,selected_tuple[4])
    entry5.delete(0,END)
    entry5.insert(END,selected_tuple[5])
    entry6.delete(0,END)
    entry6.insert(END,selected_tuple[6])
    entry7.delete(0, END)
    entry7.insert(END, selected_tuple[7])
    entry8.delete(0, END)
    entry8.insert(END, selected_tuple[8])
    entry9.delete(0, END)
    entry9.insert(END, selected_tuple[9])
    entry10.delete(0, END)
    entry10.insert(END, selected_tuple[10])
    entry11.delete(0, END)
    entry11.insert(END, selected_tuple[11])
    entry12.delete(0, END)
    entry12.insert(END, selected_tuple[12])

def view_aluno_command():
    list1.delete(0,END)
    for row in backend.view_aluno():
        list1.insert(END,row)

def view_prof_command():
    list1.delete(0,END)
    for row in backend.view_professor():
        list1.insert(END,row)

def view_disciplina_command():
    list1.delete(0,END)
    for row in backend.view_disciplina():
        list1.insert(END,row)

def view_turma_command():
    list1.delete(0,END)
    for row in backend.view_turma():
        list1.insert(END,row)

def search_aluno_command():
    list1.delete(0,END)
    for row in backend.search_aluno(name_aluno_text.get(),cpf_aluno_text.get()):
        list1.insert(END,row)

def search_prof_command():
    list1.delete(0,END)
    for row in backend.search_professor(nome_prof_text.get(),cpf_prof_text.get(),dep_prof_text.get()):
        list1.insert(END,row)

def search_disciplina_command():
    list1.delete(0,END)
    for row in backend.search_disciplina(cod_disciplina_text.get(),nome_disciplina_text.get()):
        list1.insert(END,row)

def search_turma_command():
    list1.delete(0,END)
    for row in backend.search_turma(cod_turma_text.get(),periodo_turma_text.get(),codigo_disciplina_turma.get(),cpf_prof_turma_text.get(),cpf_aluno_turma_text.get()):
        list1.insert(END,row)

def add_aluno_command():
    backend.insert_aluno(name_aluno_text.get(),cpf_aluno_text.get())
    list1.delete(0,END)
    list1.insert(END,(name_aluno_text.get(),cpf_aluno_text.get()))

def add_prof_command():
    backend.insert_professor(nome_prof_text.get(),cpf_prof_text.get(),dep_prof_text.get())
    list1.delete(0,END)
    list1.insert(END,(nome_prof_text.get(),cpf_prof_text.get(),dep_prof_text.get()))

def add_disciplina_command():
    backend.insert_disciplina(cod_disciplina_text.get(),nome_disciplina_text.get())
    list1.delete(0,END)
    list1.insert(END,(cod_disciplina_text.get(),nome_disciplina_text.get()))

def add_turma_command():
    backend.insert_turma(cod_turma_text.get(),periodo_turma_text.get(),codigo_disciplina_turma.get(),cpf_prof_turma_text.get(),cpf_aluno_turma_text.get())
    list1.delete(0,END)
    list1.insert(END,(cod_turma_text.get(),periodo_turma_text.get(),codigo_disciplina_turma.get(),cpf_prof_turma_text.get(),cpf_aluno_turma_text.get()))


def delete_aluno_command():
    backend.delete_aluno(selected_tuple[0])

def delete_prof_command():
    backend.delete_professor(selected_tuple[0])

def delete_disciplina_command():
    backend.delete_disciplina(selected_tuple[0])

def delete_turma_command():
    backend.delete_turma(selected_tuple[0])

def update_aluno_command():
    backend.update_aluno(selected_tuple[0],name_aluno_text.get(),cpf_aluno_text.get())

def update_prof_command():
    backend.update_professor(selected_tuple[0],nome_prof_text.get(),cpf_prof_text.get(),dep_prof_text.get())

def update_disciplina_command():
    backend.update_disciplina(selected_tuple[0],cod_disciplina_text.get(),nome_disciplina_text.get())

def update_turma_command():
    backend.update_turma(selected_tuple[0],cod_turma_text.get(),periodo_turma_text.get(),codigo_disciplina_turma.get(),cpf_prof_turma_text.get(),cpf_aluno_turma_text.get())

window=Tk()

label1=Label(window,text="CRUD using tkinter and sqlite3")
label1.grid(row=0,column=2)

label2=Label(window,text="Nome aluno")
label2.grid(row=1,column=0)

label3=Label(window,text="Cpf aluno")
label3.grid(row=2,column=0)

label4=Label(window,text="Nome prof")
label4.grid(row=3,column=0)

label5=Label(window,text="Cpf prof")
label5.grid(row=4,column=0)

label6=Label(window,text="Dept do prof:")
label6.grid(row=5,column=0)

label7=Label(window,text="Codigo disciplina")
label7.grid(row=6,column=0)

label8=Label(window,text="Nome disciplina")
label8.grid(row=7,column=0)

label8=Label(window,text="Codigo turma")
label8.grid(row=8,column=0)

label8=Label(window,text="periodo")
label8.grid(row=9,column=0)

label8=Label(window,text="Codigo disciplina")
label8.grid(row=10,column=0)

label8=Label(window,text="cpf prof")
label8.grid(row=11,column=0)

label8=Label(window,text="cpf aluno")
label8.grid(row=12,column=0)



name_aluno_text=StringVar()
entry1=Entry(window,textvariable=name_aluno_text)
entry1.grid(row=1,column=1)

cpf_aluno_text=StringVar()
entry2=Entry(window,textvariable=cpf_aluno_text)
entry2.grid(row=2,column=1)

nome_prof_text=StringVar()
entry3=Entry(window,textvariable=nome_prof_text)
entry3.grid(row=3,column=1)

cpf_prof_text=StringVar()
entry4=Entry(window,textvariable=cpf_prof_text)
entry4.grid(row=4,column=1)

dep_prof_text=StringVar()
entry5=Entry(window,textvariable=dep_prof_text)
entry5.grid(row=5,column=1)

cod_disciplina_text=StringVar()
entry6=Entry(window,textvariable=cod_disciplina_text)
entry6.grid(row=6,column=1)

nome_disciplina_text=StringVar()
entry7=Entry(window,textvariable=nome_disciplina_text)
entry7.grid(row=7,column=1)

cod_turma_text=StringVar()
entry8=Entry(window,textvariable=cod_turma_text)
entry8.grid(row=8,column=1)

periodo_turma_text=StringVar()
entry9=Entry(window,textvariable=periodo_turma_text)
entry9.grid(row=9,column=1)

codigo_disciplina_turma=StringVar()
entry10=Entry(window,textvariable=codigo_disciplina_turma)
entry10.grid(row=10,column=1)

cpf_prof_turma_text=StringVar()
entry11=Entry(window,textvariable=cpf_prof_text)
entry11.grid(row=11,column=1)

cpf_aluno_turma_text=StringVar()
entry12=Entry(window,textvariable=cpf_aluno_turma_text)
entry12.grid(row=12,column=1)




list1=Listbox(window,height=20,width=59)
list1.grid(row=1,column=3, rowspan=12, columnspan=2)

scrl=Scrollbar(window)
scrl.grid(row=1,column=2, sticky='ns',rowspan=6)

list1.configure(yscrollcommand=scrl.set)
scrl.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>',get_selected_row)

b1=Button(window,text="view aluno",width=12, command=view_aluno_command)
b1.grid(row=13, column=0)

b2=Button(window,text="view prof",width=12, command=view_prof_command)
b2.grid(row=13, column=1)

b3=Button(window,text="view disciplina",width=12, command=view_disciplina_command)
b3.grid(row=13, column=2)

b4=Button(window,text="view turma",width=12, command=view_turma_command)
b4.grid(row=13, column=3)

b5=Button(window,text="add aluno",width=12,command=add_aluno_command)
b5.grid(row=14, column=0)

b6=Button(window,text="add prof",width=12,command=add_prof_command)
b6.grid(row=14, column=1)

b7=Button(window,text="add disciplina",width=12,command=add_disciplina_command)
b7.grid(row=14, column=2)

b8=Button(window,text="add turma",width=12,command=add_turma_command)
b8.grid(row=14, column=3)

b9=Button(window,text="delete aluno",width=12,command=delete_aluno_command)
b9.grid(row=15, column=0)

b10=Button(window,text="delete prof",width=12,command=delete_prof_command)
b10.grid(row=15, column=1)

b11=Button(window,text="delete disciplina",width=12,command=delete_disciplina_command)
b11.grid(row=15, column=2)

b12=Button(window,text="delete turma",width=12,command=delete_turma_command)
b12.grid(row=15, column=3)

b13=Button(window,text="search aluno",width=12,command=search_aluno_command)
b13.grid(row=16, column=0)

b14=Button(window,text="search prof",width=12,command=search_prof_command)
b14.grid(row=16, column=1)

b15=Button(window,text="search disciplina",width=12,command=search_disciplina_command)
b15.grid(row=16, column=2)

b16=Button(window,text="search turma",width=12,command=search_turma_command)
b16.grid(row=16, column=3)

b17=Button(window,text="update aluno",width=12,command=update_aluno_command)
b17.grid(row=17, column=0)

b18=Button(window,text="update prof",width=12,command=update_prof_command)
b18.grid(row=17, column=1)

b19=Button(window,text="update disciplina",width=12,command=update_disciplina_command)
b19.grid(row=17, column=2)

b20=Button(window,text="update turma",width=12,command=update_turma_command)
b20.grid(row=17, column=3)





window.mainloop()