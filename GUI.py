from Tkinter import *
from functools import *
from PPP import *

# Option variables
wiremode = 0  # Wireless mode (filters 8 < less)
emode = 0  # e-mail mode
HARDmode = 0  # Hardcore mode


def define_status(obj, text):
    """
    Function to define a status to the program
    :param obj: Tkinter label object
    :param text: Status text
    :return: void
    """
    obj["text"] = "Status: {0}".format(text)
    return


def process_data_handler(name, birth, phone, telphone, keywords, output_list, lab_stat):

    # Precisa-se ter um arquivo de saida no IO
    if output_list is "":
        return define_status(lab_stat, "Sem arquivo de saida especificado.")

    # num_pass tem o numero de senhas geradas
    num_pass = process_data({
        "nome": name,
        "aniversario": birth,
        "celular": phone,
        "telefone": telphone,
        "palavras-chave": keywords
    })

    return define_status(lab_stat, "Foram geradas {0} senhas.".format(num_pass))


# def options():
#    janela2=Tk()
#    janela2.title("Options")
#    janela2.geometry("400x200+600+200")
#    lb2=Label(janela2,text="options config here\n ")
#    lb2.place(x=25, y=50)
#    lb3 = Label(janela2, text="and here ")
#    lb3.place(x=105, y=100)
#    btn2=Button(janela2, width=7, text="Fechar", command=janela2.destroy)
#    btn2.place(x=150, y=150)


def help_func():
    janela2 = Tk()
    janela2.title("Help")
    janela2.geometry("400x300+600+200")
    header_label = Label(janela2, text="PPP - Personal Password Profiler")
    header_label.place(x=10, y=30)
    btn2 = Button(janela2, width=7, text="Fechar", command=janela2.destroy)
    btn2.place(x=150, y=250)


def about():
    janela2 = Tk()
    janela2.title("About")
    janela2.geometry("400x200+600+200")
    lb2 = Label(janela2, text="About text here\n  ")
    lb2.place(x=15, y=50)
    lbcr = Label(janela2, text="\n  ")
    lbcr.place(x=105, y=100)
    btn2 = Button(janela2, width=7, text="Fechar", command=janela2.destroy)
    btn2.place(x=150, y=150)


janela = Tk()
janela.title("PPP - Personal Password Profiler")

principal = Menu(janela)
arquivo = Menu(principal)
# principal.add_command(label="options", command=options)
principal.add_command(label="Ajuda", command=help_func)
principal.add_command(label="Sobre", command=about)

janela.configure(menu=principal)

lb = Label(janela, text="Coleta de dados pessoais")
lb.place(x=180, y=30)

lbn = Label(janela, text="Nome:")
lbn.place(x=30, y=70)

lbn = Label(janela, text="Aniversario:")
lbn.place(x=30, y=100)

lbc = Label(janela, text="Celular:")
lbc.place(x=30, y=130)

lbtf = Label(janela, text="Telefone fixo:")
lbtf.place(x=30, y=160)

lbpe = Label(janela, text="Palavras extras:")
lbpe.place(x=30, y=190)

lbas = Label(janela, text="Arquivo de saida:")
lbas.place(x=30, y=240)

entradan = Entry(janela, width=30, font="Arial", border=2)
entradan.place(x=200, y=70)

entradaan = Entry(janela, width=30, font="Arial", border=2)
entradaan.place(x=200, y=100)

entradac = Entry(janela, width=30, font="Arial", border=2)
entradac.place(x=200, y=130)

entradatf = Entry(janela, width=30, font="Arial", border=2)
entradatf.place(x=200, y=160)

entradape = Entry(janela, width=30, font="Arial", border=2)
entradape.place(x=200, y=190)

entrada_output = Entry(janela, width=30, font="Arial", border=2)
entrada_output.place(x=200, y=240)

labstat = Label(janela, text="Status: ")
labstat.place(x=30, y=370)

bt2 = Button(janela, width=20, text="Gerar")
bt2["command"] = partial(process_data_handler, entradan.get(), entradaan.get(), entradac.get(), entradatf.get(),
                         entradape.get(), entrada_output.get(), labstat)
bt2.place(x=150, y=330)

C1 = Checkbutton(janela, text=" Modo wireless", variable=wiremode, onvalue=1, offvalue=0)
C1.place(x=330, y=280)

C2 = Checkbutton(janela, text="Modo E-mail", variable=emode, onvalue=1, offvalue=0)
C2.place(x=200, y=280)

C3 = Checkbutton(janela, text="Modo HARDCORE", variable=HARDmode, onvalue=1, offvalue=0)
C3.place(x=30, y=280)

janela.geometry("500x400+200+200")
janela.mainloop()
