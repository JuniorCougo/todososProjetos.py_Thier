import tkinter as tk
from tkinter import simpledialog

# Cores
cor1 = "#0a0a0a"  # black / preta
cor2 = "#fafcff"  # white / branca
cor3 = "#21c25c"  # green / verde
cor4 = "#eb463b"  # red / vermelha
cor5 = "#dedcdc"  # gray / Cizenta
cor6 = "#3080f0"  # blue / azul

class Stopwatch:
    def __init__(self, root):
        self.root = root
        self.root.title("Cronômetro")

        self.running = False
        self.time_elapsed = 0
        self.countdown_time = None

        self.label = tk.Label(root, text="00:00:00", font=("Helvetica", 48), bg=cor1, fg=cor6)
        self.label.pack()

        self.start_button = tk.Button(root, text="Iniciar", command=self.start, bg=cor1, fg=cor5, font=('Ivy 8 bold'), relief='raised', overrelief='ridge')
        self.start_button.pack(side=tk.LEFT)

        self.stop_button = tk.Button(root, text="Parar", command=self.stop, bg=cor1, fg=cor5, font=('Ivy 8 bold'), relief='raised', overrelief='ridge')
        self.stop_button.pack(side=tk.LEFT)

        self.reset_button = tk.Button(root, text="Resetar", command=self.reset, bg=cor1, fg=cor5, font=('Ivy 8 bold'), relief='raised', overrelief='ridge')
        self.reset_button.pack(side=tk.LEFT)

        self.countdown_button = tk.Button(root, text="Contagem Regressiva", command=self.set_countdown, bg=cor1, fg=cor5, font=('Ivy 8 bold'), relief='raised', overrelief='ridge')
        self.countdown_button.pack(side=tk.LEFT)

    def update_timer(self):
        if self.running:
            if self.countdown_time is not None:
                self.countdown_time -= 1
                if self.countdown_time <= 0:
                    self.label.config(text="00:00:00")
                    self.running = False
                    return
                time_str = self.format_time(self.countdown_time)
            else:
                self.time_elapsed += 1
                time_str = self.format_time(self.time_elapsed)
            self.label.config(text=time_str)
            self.root.after(1000, self.update_timer)  # Atualiza a cada segundo

    def start(self):
        if not self.running:
            self.running = True
            self.update_timer()

    def stop(self):
        self.running = False

    def reset(self):
        self.running = False
        self.time_elapsed = 0
        self.countdown_time = None
        self.label.config(text="00:00:00")

    def set_countdown(self):
        if not self.running:
            self.countdown_time = self.get_time_input("Insira o tempo para a contagem regressiva (em segundos):")
            if self.countdown_time is not None:
                self.label.config(text=self.format_time(self.countdown_time))

    def get_time_input(self, prompt):
        try:
            time = simpledialog.askinteger("Tempo", prompt)
            return time if time is not None and time > 0 else None
        except ValueError:
            return None

    def format_time(self, seconds):
        hrs, secs = divmod(seconds, 3600)
        mins, secs = divmod(secs, 60)
        return f"{hrs:02}:{mins:02}:{secs:02}"

if __name__ == "__main__":
    root = tk.Tk()
    root.configure(bg=cor1)  # Configura a cor de fundo da janela principal
    stopwatch = Stopwatch(root)
    root.mainloop()

