''' 
Pessoa 1: Luiza 
Ɛ> ════════════════════════════════════════════════════════ <3
                            Main
Ɛ> ════════════════════════════════════════════════════════ <3

--> Sempre que quiser rodar o código tem que ser por aqui!
'''
import os # biblioteca para trabalhar com caminhos de arquivos
import customtkinter as ctk # biblioteca da interface gráfica
from utils.theme import COLORS # importa nosso dicionário de cores
from customtkinter import CTkImage # classe específica para carregar imagens
from PIL import Image # biblioteca para abrir arquivos PNG

# Importa cada tela pelo nome
from views.home import HomeView
from views.financeiro import FinanceiroView
from views.todo import TodoView
from views.calendario import CalendarioView
from views.pomodoro import PomodoroView

# --- Configuração global --------------- 

ctk.set_appearance_mode("System")  #modo claro por padrão    
ctk.set_default_color_theme("blue")


def carregar_icone(nome, tamanho=(22, 22)): # Pega o caminho absoluto da pasta onde o main.py está
    base = os.path.dirname(os.path.abspath(__file__))
    caminho = os.path.join(base, "icons", f"{nome}.png") # Monta o caminho completo até o PNG
    imagem = Image.open(caminho)
    return CTkImage(light_image=imagem, size=tamanho)

class App(ctk.CTk):  #Classe principal do app
    def __init__(self):
        super().__init__() # inicializa a janela antes de qualquer coisa
        
# --- Configurações básicas da janela ------ 

        self.title("Organizador pessoal inteligente") # título na barra do sistema
        self.geometry("1200x750") #largura x altura 
        self.minsize(1000, 650) #menor tamanho permitido ao redimensionar
        self.configure(fg_color=COLORS["bg"]) #cor de fundo da janela
        
        self.dark_mode = False # controla o tema atual
        self.current_view = None # guarda a tela atual para poder destruí-la ao trocar
        
        # Constrói as partes da janela em ordem
        self._build_layout()
        self._build_sidebar()
        self._build_topbar()
        self.show_view("home") # abre na tela inicial

    # --- Layout principal --------------
    
    # weight=1 pode crescer
    # weight=0 tamanho fixo
    
    def _build_layout(self): #divide a janela em 3 regiões
        
        self.grid_columnconfigure(0, weight=0)  # sidebar 
        self.grid_columnconfigure(1, weight=1)  # conteúdo 
        self.grid_rowconfigure(0, weight=0)     # topbar 
        self.grid_rowconfigure(1, weight=1)     # conteúdo 

        # (sidebar)
        self.sidebar = ctk.CTkFrame(
            self, 
            width=220,# larguyra
            corner_radius=0, # sem arredondamento 
            fg_color=COLORS["sidebar"] # cor
        )
        self.sidebar.grid(row=0, column=0, rowspan=2, sticky="nsew")
        self.sidebar.grid_propagate(False)  # mantém largura fixa 

        # (topbar)
        self.topbar = ctk.CTkFrame(
            self,
            height=60, #altura
            corner_radius=0, # sem borda arredondada
            fg_color=COLORS["bg"] # cor
        )
        self.topbar.grid(row=0, column=1, sticky="ew")
        self.topbar.grid_propagate(False)  # mantém altura fixa 

        # (conteudo)
        self.content = ctk.CTkFrame(
            self,
            corner_radius=0, # sem borda arredondada
            fg_color=COLORS["bg"] # cor
        )
        self.content.grid(row=1, column=1, sticky="nsew", padx=24, pady=(0, 24))
        self.content.grid_columnconfigure(0, weight=1)
        self.content.grid_rowconfigure(0, weight=1)

# --- Sidebar -------------------
    
    # menu lateral
    def _build_sidebar(self): 

        # logo
        logo_frame = ctk.CTkFrame(self.sidebar, fg_color="transparent")
        logo_frame.pack(pady=(28, 20), padx=20, fill="x") #ocupa toda a largura da sidebar

        ctk.CTkLabel(
            logo_frame,
            text="???", #logo
            font=("Segoe UI", 28), #fonte 
            text_color=COLORS["btn_primario"] #cor
        ).pack(side="left", padx=(0, 8)) # empurra para a esquerda e 8 pixels de espaço à direita

        ctk.CTkLabel(
            logo_frame,
            text="Organizador pessoal", #titulo
            font=("Segoe UI", 18, "bold"),#fonte
            text_color=COLORS["text_primario"] # cor
        ).pack(side="left") #posição

        # Linha separadora
        ctk.CTkFrame(
            self.sidebar,
            height=1, # altura
            fg_color=COLORS["card_border"] # cor
        ).pack(fill="x", padx=16, pady=(0, 16))

        # Botões de navegação
        self.nav_buttons = {} # Dicionário para guardar referência de cada botão

        nav_items = [
            ("home",       "home",       "Início"),
            ("financeiro", "financeiro", "Financeiro"),
            ("todo",       "todo",       "To-do List"),
            ("calendario", "calendario", "Calendário"),
            ("pomodoro",   "pomodoro",   "Pomodoro"),
        ]
        
        # Frame que agrupa todos os botões
        nav_frame = ctk.CTkFrame(self.sidebar, fg_color="transparent")
        nav_frame.pack(fill="x", padx=12)

        for key, icone_nome, label in nav_items: #cria um botão para cada item da lista acima
            icone = carregar_icone(icone_nome)# Carrega o PNG correspondente da pasta icons/

            btn = ctk.CTkButton(
                nav_frame,
                text=f"   {label}", # espaço para o ícone
                image=icone, # PNG carregado acima
                compound="left",# imagem à esquerda do texto
                anchor="w",# texto alinhado à esquerda 
                height=44, # altura
                corner_radius=10, #bordas
                font=("Segoe UI", 14), # fonte
                fg_color="transparent",
                hover_color=COLORS["nav_hover"],
                text_color=COLORS["text_secundario"],
                command=lambda k=key: self.show_view(k) #sem isso todos os botões abririam a última tela
            )
            btn.pack(fill="x", pady=3)# botão ocupa toda a largura do nav_frame
            # pady=3 dá um espaço entre os botões

            self.nav_buttons[key] = btn # Salva referência

        # Botão de dark mode no rodapé
        bottom_frame = ctk.CTkFrame(self.sidebar, fg_color="transparent")
        bottom_frame.pack(side="bottom", fill="x", padx=12, pady=20)

        # Linha separadora acima do botão de tema
        ctk.CTkFrame(
            self.sidebar,
            height=1,
            fg_color=COLORS["card_border"]
        ).pack(side="bottom", fill="x", padx=16)

        # Carrega os ícones de lua e sol 
        self.icone_lua = carregar_icone("moon")  # modo escuro
        self.icone_sol = carregar_icone("sun")   # modo claro

        self.theme_btn = ctk.CTkButton(# Salvamos em self. para poder trocar o ícone em toggle_theme()
            bottom_frame,
            text="   Modo Escuro",
            image=self.icone_lua, # começa com ícone de lua (modo claro ativo)
            compound="left", # ícone à esquerda do texto
            anchor="w",
            height=44,
            corner_radius=10,
            font=("Segoe UI", 14),
            fg_color="transparent",
            hover_color=COLORS["nav_hover"],
            text_color=COLORS["text_secundario"],
            command=self.toggle_theme
        )
        self.theme_btn.pack(fill="x")# trocar texto e ícone em toggle_theme()

    # --- Topbar ------------------
    def _build_topbar(self): #Barra superior com o título da página atual.

        self.topbar.grid_columnconfigure(0, weight=1)

        self.page_title = ctk.CTkLabel(
            self.topbar,
            text="Início",
            font=("Segoe UI", 20, "bold"),
            text_color=COLORS["text_primario"]
        )
        self.page_title.grid(row=0, column=0, padx=24, pady=16, sticky="w")

    # --- Navegação ------------------
    def show_view(self, key: str): #Troca a tela exibida na área de conteúdo  

        # [1] visual dos botões  
        for k, btn in self.nav_buttons.items(): #destaca o ativo e apaga os outros
            if k == key:
                btn.configure(
                    fg_color=COLORS["nav_active"],
                    text_color=COLORS["text_primario"],
                    font=("Segoe UI", 14, "bold")
                )
            else:
                btn.configure(
                    fg_color="transparent",
                    text_color=COLORS["text_secundario"],
                    font=("Segoe UI", 14)
                )

        #[2] Remove a tela atual da memória
        if self.current_view:
            self.current_view.destroy()

        #[3] Atualiza o título na topbar
        titles = {
            "home":       "Início",
            "financeiro": "Financeiro",
            "todo":       "To-do List",
            "calendario": "Calendário",
            "pomodoro":   "Pomodoro",
        }
        self.page_title.configure(text=titles[key])

        # [4] Cria e exibe a nova tela
        views = {
            "home":       HomeView,
            "financeiro": FinanceiroView,
            "todo":       TodoView,
            "calendario": CalendarioView,
            "pomodoro":   PomodoroView,
        }
        ViewClass = views[key]  # pega a classe pelo nome
        self.current_view = ViewClass(self.content) # instancia a tela
        self.current_view.grid(row=0, column=0, sticky="nsew")

    # --- Tema ----------------
    def toggle_theme(self): #Alterna entre modo claro e escuro.

        self.dark_mode = not self.dark_mode

        if self.dark_mode:
            ctk.set_appearance_mode("dark")
            self.theme_btn.configure(text="     Modo Claro")
        else:
            ctk.set_appearance_mode("light")
            self.theme_btn.configure(text="     Modo Escuro")

        # renderiza a tela atual com o novo tema
        current_key = next(
            (k for k, btn in self.nav_buttons.items()
            if btn.cget("fg_color") == COLORS["nav_active"]), "home"
        )
        self.show_view(current_key)


# --- Ponto de entrada ----------------
if __name__ == "__main__": # Esse bloco só executa se você rodar este arquivo diretamente.
    app = App()
    app.mainloop()  # loop que mantém a janela aberta
