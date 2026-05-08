import customtkinter as ctk
from tkinter import filedialog, messagebox
import pandas as pd
import os
import ctypes # Para Enganar o Windows




class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Forçar Inicio Barra titulo
        self.after(10, self.mostrar_na_barra_de_tarefas)


        # Configurações Iniciais
        self.title("Calculadora - Média Escolar")
        self.overrideredirect(True)
        self.geometry("400x400")
        ctk.set_appearance_mode("light")

        # --- BARRA DE TÍTULO PERSONALIZADA ---
        self.barra_titulo = ctk.CTkFrame(self, height=35, fg_color="#000000", corner_radius=0)
        self.barra_titulo.pack(fill="x", side="top")

        self.btn_fechar = ctk.CTkButton(self.barra_titulo, text="✕", width=35, height=35,
                                        fg_color="transparent", hover_color="#e81123",
                                        corner_radius=0, command=self.destroy)
        self.btn_fechar.pack(side="right")

        self.label_janela = ctk.CTkLabel(self.barra_titulo, text="Média Escolar", font=("Roboto", 12, "bold"), text_color="#ffffff")
        self.label_janela.pack(side="left", padx=10)

        self.barra_titulo.bind("<ButtonPress-1>", self.iniciar_arrasto)
        self.barra_titulo.bind("<B1-Motion>", self.mover_janela)

        # --- CORPO DO APLICATIVO ---
        self.corpo = ctk.CTkFrame(self, fg_color="transparent")
        self.corpo.pack(expand=True, fill="both", padx=20)

        self.titulo = ctk.CTkLabel(self.corpo, text="Cálculo de Média", font=("Roboto", 18, "bold"), text_color="#008080")
        self.titulo.pack(pady=(5, 5))

        self.entrada_nome = ctk.CTkEntry(self.corpo, placeholder_text="Nome do Aluno", width=200)
        self.entrada_nome.pack(pady=2)
       
        self.entrada1 = ctk.CTkEntry(self.corpo, placeholder_text="1º Bimestre", width=200)
        self.entrada1.pack(pady=2)
        
        self.entrada2 = ctk.CTkEntry(self.corpo, placeholder_text="2º Bimestre", width=200)
        self.entrada2.pack(pady=2)
        
        self.entrada3 = ctk.CTkEntry(self.corpo, placeholder_text="3º Bimestre", width=200)
        self.entrada3.pack(pady=2)
        
        self.entrada4 = ctk.CTkEntry(self.corpo, placeholder_text="4º Bimestre", width=200)
        self.entrada4.pack(pady=2) 

        self.calculo = ctk.CTkButton(self.corpo, text="Calcular", corner_radius=10, command=self.calcular_media)
        self.calculo.pack(pady=10)

        self.save = ctk.CTkButton(self.corpo, text="Salvar Média", corner_radius=10, fg_color="#27ae60", hover_color="#219150", command=self.salvar_excel)
        self.save.pack(pady=2)

        self.resultado = ctk.CTkLabel(self.corpo, text="Média: --", font=("Roboto", 16, "bold"))
        self.resultado.pack(pady=5)

    def iniciar_arrasto(self, event):
        self.x_off = event.x
        self.y_off = event.y

    def mover_janela(self, event):
        x = event.x_root - self.x_off
        y = event.y_root - self.y_off
        self.geometry(f'+{x}+{y}')

    def calcular_media(self):
        try:
            n1 = float(self.entrada1.get())
            n2 = float(self.entrada2.get())
            n3 = float(self.entrada3.get())
            n4 = float(self.entrada4.get())

            media = (n1 + n2 + n3 + n4) / 4
            status = "Aprovado" if media >= 6 else "Reprovado"
            cor = "#2ecc71" if media >= 6 else "#e74c3c"
            
            self.resultado.configure(text=f"{status}: {media:.1f}", text_color=cor)
            return media, status # ESSENCIAL: Retorna os valores para a função de salvar
        except ValueError:
            self.resultado.configure(text="Erro: Notas inválidas", text_color="orange")
            return None, None

    def salvar_excel(self):
        retorno = self.calcular_media()

        if retorno == (None, None):
            messagebox.showwarning("Aviso", "Verifique as notas e tente novamente!")
            return

        media, status = retorno
        nome = self.entrada_nome.get().strip()

        if not nome:
            messagebox.showwarning("Aviso", "Preencha o nome do aluno!")
            return

        caminho_arquivo = filedialog.asksaveasfilename(
            defaultextension=".xlsx",
            filetypes=[("Arquivos de Excel", "*.xlsx")],
            title="Salvar como..."
        )

        if caminho_arquivo:
            novos_dados = {
                'Nome': [nome],
                'Nota 1': [self.entrada1.get()],
                'Nota 2': [self.entrada2.get()],
                'Nota 3': [self.entrada3.get()],
                'Nota 4': [self.entrada4.get()],
                'Média Final': [f"{media:.2f}"],
                'Resultado': [status]
            }
            df = pd.DataFrame(novos_dados)

            try:
                if os.path.exists(caminho_arquivo):
                    df_antigo = pd.read_excel(caminho_arquivo)
                    df = pd.concat([df_antigo, df], ignore_index=True)
                
                df.to_excel(caminho_arquivo, index=False)
                messagebox.showinfo("Sucesso", f"Dados de {nome} salvos com sucesso!")
            except Exception as e:
                messagebox.showerror("Erro", f"Não foi possível salvar: {e}")

    def mostrar_na_barra_de_tarefas(self):
        GWL_EXSTYLE = -20
        WS_EX_APPWINDOW = 0x00040000
        WS_EX_TOOLWINDOW = 0x00000080

        hwnd = ctypes.windll.user32.GetParent(self.winfo_id())
        style = ctypes.windll.user32.GetWindowLongW(hwnd, GWL_EXSTYLE)
        
        # Remove o estilo de 'janela de ferramenta' e adiciona o de 'janela de app'
        style = (style & ~WS_EX_TOOLWINDOW) | WS_EX_APPWINDOW
        
        ctypes.windll.user32.SetWindowLongW(hwnd, GWL_EXSTYLE, style)
        
        # Força o Windows a redesenhar a janela com o novo estilo
        self.withdraw()
        self.after(10, self.deiconify)


























if __name__ == "__main__":
    app = App()
    app.mainloop()
