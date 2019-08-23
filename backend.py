import sqlite3

def connect():
    conn=sqlite3.connect("banco.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTs aluno (id INTEGER PRIMARY KEY , name TEXT , cpf TEXT)")
    cur.execute(
        "CREATE TABLE IF NOT EXISTs professor (id INTEGER PRIMARY KEY , name TEXT , cpf TEXT , departamento TEXT)")
    cur.execute(
        "CREATE TABLE IF NOT EXISTs disciplina (id INTEGER PRIMARY KEY , codigo TEXT , nome TEXT )")
    cur.execute(
        "CREATE TABLE IF NOT EXISTs turma (id INTEGER PRIMARY KEY , codigo_turma TEXT , periodo TEXT , codigo_disciplina TEXT, cpf_prof TEXT , cpf_aluno TEXT)")

    conn.commit()
    conn.close()
def insert_aluno(name,cpf):

    conn=sqlite3.connect("banco.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO aluno VALUES (NULL, ?,?)",(name,cpf))
    conn.commit()
    conn.close()
    view_aluno()

def view_aluno():
    conn=sqlite3.connect("banco.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM aluno")
    row=cur.fetchall()
    conn.close()
    return row

def search_aluno(name="",cpf=""):
    conn=sqlite3.connect("banco.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM aluno WHERE name=? OR cpf=?",(name,cpf))
    row=cur.fetchall()
    conn.close()
    return row

def delete_aluno(id):
    conn=sqlite3.connect("banco.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM aluno  where id=?",(id,))
    conn.commit()
    conn.close()

def update_aluno(id,name,cpf):

    conn=sqlite3.connect("banco.db")
    cur=conn.cursor()
    cur.execute("UPDATE aluno SET name=? ,cpf=? where id=? ",(name,cpf,id))
    conn.commit()
    conn.close()

def insert_professor(name,cpf,departamento):

    conn=sqlite3.connect("banco.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO professor VALUES (NULL, ?,?,?)",(name,cpf,departamento))
    conn.commit()
    conn.close()
    view_professor()

def view_professor():
    conn=sqlite3.connect("banco.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM professor")
    row=cur.fetchall()
    conn.close()
    return row

def search_professor(name="",cpf="",departamento=""):
    conn=sqlite3.connect("banco.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM professor WHERE name=? OR cpf=? OR departamento=?",(name,cpf,departamento))
    row=cur.fetchall()
    conn.close()
    return row

def delete_professor(id):
    conn=sqlite3.connect("banco.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM professor  where id=?",(id,))
    conn.commit()
    conn.close()

def update_professor(id,name,cpf,departamento):

    conn=sqlite3.connect("banco.db")
    cur=conn.cursor()
    cur.execute("UPDATE professor SET name=? ,cpf=? , departamento=? where id=?",(name,cpf,departamento,id))
    conn.commit()
    conn.close()

def insert_disciplina(codigo,nome):

    conn=sqlite3.connect("banco.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO disciplina VALUES (NULL, ?,?)",(codigo,nome))
    conn.commit()
    conn.close()
    view_aluno()

def view_disciplina():
    conn=sqlite3.connect("banco.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM disciplina")
    row=cur.fetchall()
    conn.close()
    return row

def search_disciplina(codigo="",nome=""):
    conn=sqlite3.connect("banco.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM disciplina WHERE codigo=? OR nome=?",(codigo,nome))
    row=cur.fetchall()
    conn.close()
    return row

def delete_disciplina(id):
    conn=sqlite3.connect("banco.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM disciplina  where id=?",(id,))
    conn.commit()
    conn.close()

def update_disciplina(id,codigo,nome):

    conn=sqlite3.connect("banco.db")
    cur=conn.cursor()
    cur.execute("UPDATE disciplina SET codigo=? ,nome=? where id=? ",(codigo,nome,id))
    conn.commit()
    conn.close()

def insert_turma(codigo_turma,periodo,codigo_disciplina,cpf_prof,cpf_aluno):

    conn=sqlite3.connect("banco.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO turma VALUES (NULL, ?,?,?,?,?)",(codigo_turma,periodo,codigo_disciplina,cpf_prof,cpf_aluno))
    conn.commit()
    conn.close()
    view_turma()

def view_turma():
    conn=sqlite3.connect("banco.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM turma")
    row=cur.fetchall()
    conn.close()
    return row

def search_turma(codigo_turma="",periodo="",codigo_disciplina="",cpf_prof="",cpf_aluno=""):
    conn=sqlite3.connect("turma.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM turma WHERE codigo_turma=? OR periodo=? OR codigo_disciplina=?  OR  cpf_prof=?  OR  cpf_aluno=?",(codigo_turma,periodo,codigo_disciplina,cpf_prof,cpf_aluno))
    row=cur.fetchall()
    conn.close()
    return row

def delete_turma(id):
    conn=sqlite3.connect("banco.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM turma  where id=?",(id,))
    conn.commit()
    conn.close()

def update_turma(id,codigo_turma,periodo,codigo_disciplina,cpf_prof,cpf_aluno):

    conn=sqlite3.connect("banco.db")
    cur=conn.cursor()
    cur.execute("UPDATE turma SET codigo_turma=? ,codigo_turma=? , periodo=? ,  codigo_disciplina=? , cpf_prof=? , cpf_aluno=? where id=?",(codigo_turma,periodo,codigo_disciplina,cpf_prof,cpf_aluno,id))
    conn.commit()
    conn.close()

connect()

