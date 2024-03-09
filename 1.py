import tkinter as tk

class Livro:
    def __init__(self, titulo, autor, id):
        self.titulo = titulo
        self.autor = autor
        self.id = id
        self.disponivel = True

class Membro:
    def __init__(self, nome, numero):
        self.nome = nome
        self.numero = numero
        self.historico = []

class Biblioteca:
    def __init__(self):
        self.catalogo = {}
        self.membros = {}

    def adicionar_livro(self, titulo, autor):
        livro = Livro(titulo, autor, len(self.catalogo) + 1) 
        self.catalogo[livro.id] = livro

    def adicionar_membro(self, nome, numero):
        membro = Membro(nome, numero)
        self.membros[numero] = membro

    def emprestar_livro(self, livro_id, membro_numero):
        livro = self.catalogo.get(livro_id)
        membro = self.membros.get(membro_numero)
        if livro and membro:
            if livro.disponivel:
                livro.disponivel = False
                membro.historico.append(livro)
                return "Empréstimo realizado."
            else:
                return "Este livro não está disponível."
        else:
            return "O livro ou o membro não existe."

    def devolver_livro(self, livro_id, membro_numero):
        livro = self.catalogo.get(livro_id)
        membro = self.membros.get(membro_numero)
        if livro and membro and livro in membro.historico:
            livro.disponivel = True
            membro.historico.remove(livro)
            return True
        else:
            return False

    def pesquisar_livro(self, parametro):
        resultados = []
        for livro in self.catalogo.values():
            if parametro.lower() in [livro.titulo.lower(), livro.autor.lower(), str(livro.id).lower()]:
                resultados.append(livro)
        return resultados

class InterfaceBiblioteca(tk.Tk):
    def __init__(self):
        super().__init__()
        self.biblioteca = Biblioteca()
        self.title("Gerenciamento de Biblioteca")
        self.geometry("600x400")

        self.label = tk.Label(self, text="Bem-vindo à Biblioteca", font=("Arial", 16, "bold"))
        self.label.pack()

        self.frame_adicionar_livro = tk.LabelFrame(self, text="Adicionar Livro", font=("Arial", 12))
        self.frame_adicionar_livro.pack(fill="both", expand="yes", padx=20, pady=10)

        self.label_titulo = tk.Label(self.frame_adicionar_livro, text="Título:", font=("Arial", 12))
        self.label_titulo.grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.entry_titulo = tk.Entry(self.frame_adicionar_livro, font=("Arial", 12))
        self.entry_titulo.grid(row=0, column=1, padx=5, pady=5)

        self.label_autor = tk.Label(self.frame_adicionar_livro, text="Autor:", font=("Arial", 12))
        self.label_autor.grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.entry_autor = tk.Entry(self.frame_adicionar_livro, font=("Arial", 12))
        self.entry_autor.grid(row=1, column=1, padx=5, pady=5)

        self.botao_adicionar_livro = tk.Button(self.frame_adicionar_livro, text="Adicionar Livro", font=("Arial", 12), command=self.adicionar_livro)
        self.botao_adicionar_livro.grid(row=2, columnspan=2, padx=5, pady=5)

        self.frame_pesquisar_livro = tk.LabelFrame(self, text="Pesquisar Livro", font=("Arial", 12))
        self.frame_pesquisar_livro.pack(fill="both", expand="yes", padx=20, pady=10)

        self.label_pesquisar = tk.Label(self.frame_pesquisar_livro, text="Pesquisar:", font=("Arial", 12))
        self.label_pesquisar.grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.entry_pesquisar = tk.Entry(self.frame_pesquisar_livro, font=("Arial", 12))
        self.entry_pesquisar.grid(row=0, column=1, padx=5, pady=5)
        self.botao_pesquisar_livro = tk.Button(self.frame_pesquisar_livro, text="Pesquisar Livro", font=("Arial", 12), command=self.pesquisar_livro)
        self.botao_pesquisar_livro.grid(row=0, column=2, padx=5, pady=5)

        self.frame_adicionar_membro = tk.LabelFrame(self, text="Adicionar Membro", font=("Arial", 12))
        self.frame_adicionar_membro.pack(fill="both", expand="yes", padx=20, pady=10)

        self.label_nome_membro = tk.Label(self.frame_adicionar_membro, text="Nome do Membro:", font=("Arial", 12))
        self.label_nome_membro.grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.entry_nome_membro = tk.Entry(self.frame_adicionar_membro, font=("Arial", 12))
        self.entry_nome_membro.grid(row=0, column=1, padx=5, pady=5)

        self.label_numero_membro = tk.Label(self.frame_adicionar_membro, text="Número do Membro:", font=("Arial", 12))
        self.label_numero_membro.grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.entry_numero_membro = tk.Entry(self.frame_adicionar_membro, font=("Arial", 12))
        self.entry_numero_membro.grid(row=1, column=1, padx=5, pady=5)

        self.botao_adicionar_membro = tk.Button(self.frame_adicionar_membro, text="Adicionar Membro", font=("Arial", 12), command=self.adicionar_membro)
        self.botao_adicionar_membro.grid(row=2, columnspan=2, padx=5, pady=5)

        self.frame_emprestimo_livro = tk.LabelFrame(self, text="Empréstimo de Livro", font=("Arial", 12))
        self.frame_emprestimo_livro.pack(fill="both", expand="yes", padx=20, pady=10)

        self.label_id_livro_emprestimo = tk.Label(self.frame_emprestimo_livro, text="ID do Livro:", font=("Arial", 12))
        self.label_id_livro_emprestimo.grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.entry_id_livro_emprestimo = tk.Entry(self.frame_emprestimo_livro, font=("Arial", 12))
        self.entry_id_livro_emprestimo.grid(row=0, column=1, padx=5, pady=5)

        self.label_numero_membro_emprestimo = tk.Label(self.frame_emprestimo_livro, text="Número do Membro:", font=("Arial", 12))
        self.label_numero_membro_emprestimo.grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.entry_numero_membro_emprestimo = tk.Entry(self.frame_emprestimo_livro, font=("Arial", 12))
        self.entry_numero_membro_emprestimo.grid(row=1, column=1, padx=5, pady=5)

        self.botao_emprestimo_livro = tk.Button(self.frame_emprestimo_livro, text="Empréstimo de Livro", font=("Arial", 12), command=self.emprestimo_livro)
        self.botao_emprestimo_livro.grid(row=2, columnspan=2, padx=5, pady=5)

        self.label_resultado_emprestimo = tk.Label(self, text="", font=("Arial", 12))
        self.label_resultado_emprestimo.pack(padx=20, pady=10)

    def adicionar_livro(self):
        titulo = self.entry_titulo.get()
        autor = self.entry_autor.get()
        self.biblioteca.adicionar_livro(titulo, autor)
        self.label.config(text="Livro adicionado: " + titulo)

    def adicionar_membro(self):
        nome = self.entry_nome_membro.get()
        numero = self.entry_numero_membro.get()
        self.biblioteca.adicionar_membro(nome, numero)
        self.label.config(text="Membro adicionado: " + nome)

    def pesquisar_livro(self):
        parametro = self.entry_pesquisar.get()
        resultados = self.biblioteca.pesquisar_livro(parametro)
        if resultados:
            lista_resultados = "\n".join([livro.titulo for livro in resultados])
            self.label.config(text="Resultados da pesquisa:\n" + lista_resultados)
        else:
            self.label.config(text="Nenhum resultado encontrado para: " + parametro)

    def emprestimo_livro(self):
        try:
            livro_id = int(self.entry_id_livro_emprestimo.get())
            membro_numero = int(self.entry_numero_membro_emprestimo.get())
            resultado = self.biblioteca.emprestar_livro(livro_id, membro_numero)
            self.label_resultado_emprestimo.config(text=resultado)
        except ValueError:
            self.label_resultado_emprestimo.config(text="Por favor, insira valores numéricos para o ID do livro e número do membro.")

if __name__ == "__main__":
    app = InterfaceBiblioteca()
    app.mainloop()
