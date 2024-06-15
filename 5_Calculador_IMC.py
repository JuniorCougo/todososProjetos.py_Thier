from tkinter import *
from tkinter import ttk

cor0 = '#ffffff'  # Branco
cor1 = '#444466'  # Preto
cor2 = '#4065a1'  # Azul

janela = Tk()
janela.title('')
janela.geometry('295x360')  # Aumentei a altura para acomodar melhor as mensagens
janela.configure(bg='white')

frame_cima = Frame(janela, width=295, height=50, bg=cor0, pady=0, padx=0, relief='flat')
frame_cima.grid(row=0, column=0, sticky=NSEW)

frame_baixo = Frame(janela, width=295, height=310, bg=cor0, pady=0, padx=0, relief='flat')
frame_baixo.grid(row=1, column=0, sticky=NSEW)

app_nome = Label(frame_cima, text='Calculadora de IMC', width=23, height=1, padx=0, relief='flat', anchor='center',
                 font=('Ivy 16 bold'), bg=cor0, fg=cor1)
app_nome.place(x=0, y=0)

app_linha = Label(frame_cima, text='', width=400, height=1, padx=0, relief='flat', anchor='center', font=('Ivy 1'),
                  bg=cor2, fg=cor2)
app_linha.place(x=0, y=35)

# Adicionando novos elementos: nome, idade, sexo e mensagem de boas-vindas

l_nome = Label(frame_baixo, text='Nome:', height=1, padx=5, relief='flat', anchor='w', font=('Ivy 10 bold'),
               bg=cor0, fg=cor1)
l_nome.grid(row=0, column=0, sticky=W, pady=10, padx=3)
e_nome = Entry(frame_baixo, width=20, relief='solid', font=('Ivy 10 bold'))
e_nome.grid(row=0, column=1, sticky=W, pady=10, padx=3)

l_idade = Label(frame_baixo, text='Idade:', height=1, padx=5, relief='flat', anchor='w', font=('Ivy 10 bold'),
                bg=cor0, fg=cor1)
l_idade.grid(row=1, column=0, sticky=W, pady=10, padx=3)
e_idade = Entry(frame_baixo, width=5, relief='solid', font=('Ivy 10 bold'), justify='center')
e_idade.grid(row=1, column=1, sticky=W, pady=10, padx=3)

l_sexo = Label(frame_baixo, text='Sexo:', height=1, padx=5, relief='flat', anchor='w', font=('Ivy 10 bold'),
               bg=cor0, fg=cor1)
l_sexo.grid(row=2, column=0, sticky=W, pady=10, padx=3)
sexo_var = StringVar()
sexo_combobox = ttk.Combobox(frame_baixo, width=18, textvariable=sexo_var, state='readonly',
                             font=('Ivy 10 bold'))
sexo_combobox['values'] = ('Masculino', 'Feminino')
sexo_combobox.current(0)  # Define o valor padrão como Masculino
sexo_combobox.grid(row=2, column=1, sticky=W, pady=10, padx=3)

l_boas_vindas = Label(frame_baixo, text='', width=37, height=3, padx=0, pady=12, relief='flat', anchor='nw',
                      font=('Ivy 10 bold'), bg=cor0, fg=cor1, wraplength=270)
l_boas_vindas.grid(row=3, column=0, columnspan=2, pady=5)

def calcular():
    try:
        peso = float(e_peso.get().replace(',', '.'))  # Substitui vírgula por ponto, se houver
        altura = float(e_altura.get().replace(',', '.'))  # Substitui vírgula por ponto, se houver
        nome = e_nome.get()
        idade = int(e_idade.get())
        sexo = sexo_var.get()

        imc = peso / altura**2
        resultado = imc

        if resultado < 18.5:
            mensagem = 'abaixo do peso'
        elif resultado < 25:
            mensagem = 'com peso normal'
        elif resultado < 30:
            mensagem = 'com sobrepeso'
        else:
            mensagem = 'com obesidade'

        if sexo == 'Masculino':
            saudacao = f'Olá, {nome}! Você tem {idade} anos e está {mensagem}.'
        else:
            saudacao = f'Olá, {nome}! Você tem {idade} anos e está {mensagem}.'

        l_boas_vindas.config(text=saudacao)
        l_resultado['text'] = "{:.{}f}".format(resultado, 2)

    except ValueError:
        l_boas_vindas.config(text='Por favor, verifique os valores inseridos.')

def resetar():
    e_nome.delete(0, END)
    e_idade.delete(0, END)
    sexo_combobox.current(0)
    e_peso.delete(0, END)
    e_altura.delete(0, END)
    l_boas_vindas.config(text='')
    l_resultado.config(text='---')

l_peso = Label(frame_baixo, text='Insira Seu Peso:', height=1, padx=5, relief='flat', anchor='w', font=('Ivy 10 bold'),
               bg=cor0, fg=cor1)
l_peso.grid(row=4, column=0, sticky=W, pady=10, padx=3)
e_peso = Entry(frame_baixo, width=10, relief='solid', font=('Ivy 10 bold'), justify='center')
e_peso.grid(row=4, column=1, sticky=W, pady=10, padx=3)

l_altura = Label(frame_baixo, text='Insira Sua Altura:', height=1, padx=5, relief='flat', anchor='w',
                 font=('Ivy 10 bold'), bg=cor0, fg=cor1)
l_altura.grid(row=5, column=0, sticky=W, pady=10, padx=3)
e_altura = Entry(frame_baixo, width=10, relief='solid', font=('Ivy 10 bold'), justify='center')
e_altura.grid(row=5, column=1, sticky=W, pady=10, padx=3)

l_resultado = Label(frame_baixo, text='---', width=5, height=1, padx=6, pady=12, relief='flat', anchor='center',
                    font=('Ivy 24 bold'), bg=cor2, fg=cor0)
l_resultado.grid(row=6, column=0, columnspan=2, pady=10)

b_calcular = Button(frame_baixo, command=calcular, text='CALCULAR', width=34, height=1, overrelief=SOLID,
                    relief='raised', anchor='center', font=('Ivy 10 bold'), bg=cor2, fg=cor0)
b_calcular.grid(row=7, column=0, sticky=NSEW, pady=20, padx=5, columnspan=2)

b_resetar = Button(frame_baixo, command=resetar, text='RESETAR', width=34, height=1, overrelief=SOLID,
                    relief='raised', anchor='center', font=('Ivy 10 bold'), bg=cor2, fg=cor0)
b_resetar.grid(row=8, column=0, sticky=NSEW, pady=10, padx=5, columnspan=2)

janela.mainloop()


