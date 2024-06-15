import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import pandas as pd

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tarefas")

        # Elementos da interface gráfica
        self.label_task = tk.Label(root, text="Digite uma nova tarefa:")
        self.label_task.pack(pady=5)

        self.task_entry = tk.Entry(root, width=50)
        self.task_entry.pack(pady=5)

        self.label_start_date = tk.Label(root, text="Data de Início (DD/MM/YYYY):")
        self.label_start_date.pack(pady=5)

        self.start_date_entry = tk.Entry(root, width=50)
        self.start_date_entry.pack(pady=5)

        self.label_end_date = tk.Label(root, text="Data de Término (DD/MM/YYYY):")
        self.label_end_date.pack(pady=5)

        self.end_date_entry = tk.Entry(root, width=50)
        self.end_date_entry.pack(pady=5)

        self.add_button = tk.Button(root, text="Adicionar Tarefa", command=self.add_task)
        self.add_button.pack(pady=5)

        self.tasks_listbox = tk.Listbox(root, width=100, height=10)
        self.tasks_listbox.pack(pady=5)

        self.remove_button = tk.Button(root, text="Remover Tarefa", command=self.remove_task)
        self.remove_button.pack(pady=5)

        self.complete_button = tk.Button(root, text="Marcar como Concluída", command=self.complete_task)
        self.complete_button.pack(pady=5)

        self.label_save_path = tk.Label(root, text="Caminho para salvar o arquivo Excel:")
        self.label_save_path.pack(pady=5)

        self.save_path_entry = tk.Entry(root, width=50)
        self.save_path_entry.pack(pady=5)

        self.export_button = tk.Button(root, text="Exportar para Excel", command=self.export_to_excel)
        self.export_button.pack(pady=5)

        self.tasks = []

    def add_task(self):
        task = self.task_entry.get()
        start_date_str = self.start_date_entry.get()
        end_date_str = self.end_date_entry.get()
        
        if task and start_date_str and end_date_str:
            try:
                start_date = datetime.strptime(start_date_str, "%d/%m/%Y")
                end_date = datetime.strptime(end_date_str, "%d/%m/%Y")
                
                if end_date < start_date:
                    messagebox.showwarning("Data Inválida", "A data de término deve ser posterior à data de início.")
                    return
                
                days_to_execute = (end_date - start_date).days
                days_remaining = (end_date - datetime.now()).days

                task_info = {
                    "task": task,
                    "start_date": start_date_str,
                    "end_date": end_date_str,
                    "days_to_execute": days_to_execute,
                    "days_remaining": max(days_remaining, 0),
                    "completed": False
                }

                self.tasks.append(task_info)
                self.update_tasks_listbox()
                self.clear_entries()
            except ValueError:
                messagebox.showwarning("Data Inválida", "Por favor, insira as datas no formato DD/MM/YYYY.")
        else:
            messagebox.showwarning("Entrada Incompleta", "Por favor, preencha todos os campos.")

    def remove_task(self):
        try:
            selected_task_index = self.tasks_listbox.curselection()[0]
            del self.tasks[selected_task_index]
            self.update_tasks_listbox()
        except IndexError:
            messagebox.showwarning("Nenhuma tarefa selecionada", "Selecione uma tarefa para remover.")

    def complete_task(self):
        try:
            selected_task_index = self.tasks_listbox.curselection()[0]
            self.tasks[selected_task_index]["completed"] = True
            self.update_tasks_listbox()
        except IndexError:
            messagebox.showwarning("Nenhuma tarefa selecionada", "Selecione uma tarefa para marcar como concluída.")

    def export_to_excel(self):
        save_path = self.save_path_entry.get()
        if save_path:
            if not save_path.endswith(".xlsx"):
                save_path += ".xlsx"
            try:
                df = pd.DataFrame(self.tasks)
                df.to_excel(save_path, index=False)
                messagebox.showinfo("Sucesso", f"Tarefas exportadas para {save_path} com sucesso.")
            except Exception as e:
                messagebox.showerror("Erro", f"Falha ao exportar tarefas: {e}")
        else:
            messagebox.showwarning("Caminho inválido", "Por favor, insira um caminho válido para salvar o arquivo.")

    def update_tasks_listbox(self):
        self.tasks_listbox.delete(0, tk.END)
        for idx, task_info in enumerate(self.tasks):
            status = "Concluída" if task_info["completed"] else "Pendente"
            task_display = (
                f"{idx + 1}. Tarefa: {task_info['task']} | "
                f"Início: {task_info['start_date']} | "
                f"Término: {task_info['end_date']} | "
                f"Dias para executar: {task_info['days_to_execute']} | "
                f"Dias restantes: {task_info['days_remaining']} | "
                f"Status: {status}"
            )
            self.tasks_listbox.insert(tk.END, task_display)

    def clear_entries(self):
        self.task_entry.delete(0, tk.END)
        self.start_date_entry.delete(0, tk.END)
        self.end_date_entry.delete(0, tk.END)
        self.save_path_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()
