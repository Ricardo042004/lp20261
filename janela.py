from tkinter import Tk, Label, Entry, Button, messagebox
janela = Tk()
janela.title('Janela de Exemplo')
''
lbl_nome = Label(text=('Nome: ')
lbl_nome.grid(row=0,column=0)
global txt_nome
txt_nome = Entry(width=20)
txt_nome.grid(row=0, column=1)
def ola():
    messagebox.showinfo(title='Olá',message=f'Olá {txt_nome.get()}')

ola()
btn_ola = Button(text='Diga olá',command=ola)
btn_ola.grid(row=1,column=0)
janela.config(padx=10,pady=10)
lbl_nome.config(pady=20)