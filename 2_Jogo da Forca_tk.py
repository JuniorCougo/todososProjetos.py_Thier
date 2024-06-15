import tkinter as tk
import random

def escolher_palavra():
    palavras = ["estacio","analise" "desenvolvimento de sistemas","desenvolvimento", "tecnologia", "lógica", "programação", "inovação"]
    return random.choice(palavras)


def exibir_forca(tentativas):
    estagios = [
        """
           ------
           |    |
           |    
           |   
           |    
           |    
        --------
        """,
        """
           ------
           |    |
           |    O
           |   
           |    
           |    
        --------
        """,
        """
           ------
           |    |
           |    O
           |    |
           |    
           |    
        --------
        """,
        """
           ------
           |    |
           |    O
           |   /|
           |    
           |    
        --------
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |    
           |    
        --------
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |   / 
           |    
        --------
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |   / \\
           |    
        --------
        """
    ]
    forca_label.config(text=estagios[tentativas])

# Função para reiniciar o jogo
def reiniciar_jogo():
    global palavra, palavra_oculta, tentativas, letras_tentadas
    palavra = escolher_palavra()
    palavra_oculta = ["_"] * len(palavra)
    tentativas = 0
    letras_tentadas = []
    exibir_forca(tentativas)
    palavra_label.config(text=" ".join(palavra_oculta))
    letras_tentadas_label.config(text="")
    mensagem_label.config(text="")

# Função para adivinhar uma letra
def adivinhar():
    global tentativas
    letra = entrada_letra.get().lower()
    entrada_letra.delete(0, tk.END)

    if len(letra) != 1 or not letra.isalpha():
        mensagem_label.config(text="Por favor, insira uma única letra.")
        return

    if letra in letras_tentadas:
        mensagem_label.config(text="Você já tentou essa letra. Tente outra.")
        return

    letras_tentadas.append(letra)

    if letra in palavra:
        for i, l in enumerate(palavra):
            if l == letra:
                palavra_oculta[i] = letra
        mensagem_label.config(text="Boa! Você acertou uma letra.")
    else:
        tentativas += 1
        mensagem_label.config(text="Errado! Tente novamente.")

    exibir_forca(tentativas)
    palavra_label.config(text=" ".join(palavra_oculta))
    letras_tentadas_label.config(text="Letras tentadas: " + ", ".join(letras_tentadas))

    if "_" not in palavra_oculta:
        mensagem_label.config(text="Parabéns! Você ganhou!")
    elif tentativas >= 6:
        mensagem_label.config(text=f"Você perdeu! A palavra era: {palavra}")

# Configuração da janela principal
janela = tk.Tk()
janela.title("Jogo da Forca")

# Labels e entradas
forca_label = tk.Label(janela, text="", font=("Courier", 20))
forca_label.pack()

palavra_label = tk.Label(janela, text="", font=("Courier", 20))
palavra_label.pack()

mensagem_label = tk.Label(janela, text="", font=("Helvetica", 14))
mensagem_label.pack()

entrada_letra = tk.Entry(janela, font=("Helvetica", 14))
entrada_letra.pack()

botao_adivinhar = tk.Button(janela, text="Adivinhar", command=adivinhar)
botao_adivinhar.pack()

letras_tentadas_label = tk.Label(janela, text="", font=("Helvetica", 14))
letras_tentadas_label.pack()

botao_reiniciar = tk.Button(janela, text="Reiniciar Jogo", command=reiniciar_jogo)
botao_reiniciar.pack()

# Inicialização do jogo
reiniciar_jogo()

# Iniciar o loop principal da interface gráfica
janela.mainloop()
