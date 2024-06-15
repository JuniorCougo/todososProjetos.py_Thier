import tkinter as tk

def atualizar_expressao(valor):
    expressao.set(expressao.get() + str(valor))

def calcular():
    try:
        resultado.set(str(eval(expressao.get())))
        expressao.set("")
    except Exception as e:
        resultado.set("Erro")
        expressao.set("")

def limpar():
    expressao.set("")
    resultado.set("")

root = tk.Tk()
root.title("Calculadora")

# Adicionando mensagem de boas-vindas
mensagem_boas_vindas = "Olá, seja bem-vindo à calculadora Python\nAlunos: José Martins Jr e Luiz Felipe"
tk.Label(root, text=mensagem_boas_vindas, font=('Helvetica', 14)).grid(row=0, column=0, columnspan=4, padx=20, pady=10)

expressao = tk.StringVar()
resultado = tk.StringVar()

tk.Entry(root, textvariable=expressao, font=('Helvetica', 18), bd=10, insertwidth=4, width=14, borderwidth=4).grid(row=1, column=0, columnspan=4)
tk.Entry(root, textvariable=resultado, font=('Helvetica', 18), bd=10, insertwidth=4, width=14, borderwidth=4, state='readonly').grid(row=2, column=0, columnspan=4)

numeros = [
    ('7', 3, 0), ('8', 3, 1), ('9', 3, 2),
    ('4', 4, 0), ('5', 4, 1), ('6', 4, 2),
    ('1', 5, 0), ('2', 5, 1), ('3', 5, 2), 
    ('0', 6, 1)
]

for (text, row, col) in numeros:
    tk.Button(root, text=text, padx=20, pady=20, font=('Helvetica', 18), command=lambda t=text: atualizar_expressao(t)).grid(row=row, column=col)

operacoes = [
    ('+', 3, 3), ('-', 4, 3), ('*', 5, 3), ('/', 6, 3),
    ('C', 6, 0), ('=', 6, 2)
]

for (text, row, col) in operacoes:
    if text == '=':
        tk.Button(root, text=text, padx=20, pady=20, font=('Helvetica', 18), command=calcular).grid(row=row, column=col)
    elif text == 'C':
        tk.Button(root, text=text, padx=20, pady=20, font=('Helvetica', 18), command=limpar).grid(row=row, column=col)
    else:
        tk.Button(root, text=text, padx=20, pady=20, font=('Helvetica', 18), command=lambda t=text: atualizar_expressao(t)).grid(row=row, column=col)

root.mainloop()
