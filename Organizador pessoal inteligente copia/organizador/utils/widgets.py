''' 
Pessoa 1: Luiza 
Ɛ> ════════════════════════════════════════════════════════ <3
                            Widgets
Ɛ> ════════════════════════════════════════════════════════ <3

--> Widgets são os elementos visuais que compõem a interface do 
app, fiz a mesma coisa que o theme,so que em vez de cores, é para
os botões 

'''
import customtkinter as ctk
from utils.theme import COLORS

    # === Cards ========== (card é uma "caixa" que agrupa informações )

def Card(parent, **kwargs): #permite passar configurações extras opcionais
    return ctk.CTkFrame(
        parent,
        fg_color=kwargs.pop("fg_color", COLORS["card"]), # Cor
        corner_radius=kwargs.pop("corner_radius", 14), # Cantos arredondados
        border_width=kwargs.pop("border_width", 1), # tamanho da bordar
        border_color=kwargs.pop("border_color", COLORS["card_border"]), # cor da borda
        **kwargs  # repassa qualquer outra configuração extra
    )

    # === Botões ======== (elemento clicável que executa uma ação)

    #[1] botão para ações principais ( ex: salvar)
def PrimaryButton(parent, text, command=None, **kwargs):
    return ctk.CTkButton(
        parent,
        text=text,
        command=command,
        fg_color=COLORS["btn_primario"],  # Cor de fundo  do botão   
        hover_color=COLORS["btn_primario_hover"], # Cor ao passar o mouse por cima  
        text_color=COLORS["btn_primario_text"],   # Cor do texto   
        font=("Segoe UI", 13, "bold"),  #nome da fonte, tamanho e em negrito
        corner_radius=10,  #cantos arredondados
        height=38,  # atura
        **kwargs # Permite personalizar além do padrão
    )

    #[2] botão para ações secundárias
def SecondaryButton(parent, text, command=None, **kwargs): 
    return ctk.CTkButton(
        parent,
        text=text,
        command=command,
        fg_color=COLORS["btn_secundario"], # Cor de fundo  do botão           
        hover_color=COLORS["btn_secundario_hover"],  # Cor ao passar o mouse por cima  
        text_color=COLORS["btn_secundario_text"], # Cor do texto   
        font=("Segoe UI", 13), #nome da fonte e tamanho 
        corner_radius=10, # Cantos arredondados
        height=38, # Altura
        **kwargs # Permite personalizar além do padrão
    )

    # --- Textos --------(usado para títulos e informações)

    # [1] título grande e em negrito 
def SectionTitle(parent, text, **kwargs): 
    return ctk.CTkLabel(
        parent,
        text=text,
        font=("Segoe UI", 16, "bold"), # Tamanho 16 com negrito
        text_color=COLORS["text_primario"], # cor do texto
        **kwargs
    )

    # [2] informações secundárias (Textos de apoio que não precisam de destaque)
def MutedLabel(parent, text, **kwargs): # Cria um texto apagado (muted) para informações secundárias
    return ctk.CTkLabel(
        parent,
        text=text,
        font=("Segoe UI", 12), # nome da fonte e tamanho 
        text_color=COLORS["text_muted"], # cor do texto
        **kwargs
    )

    # --- Badge  --------( mini etiqueta colorida que indica um status)
def Badge(parent, text, color_key="success", **kwargs): 

    colors = { # mini dicionário interno que mapeia cor de fundo e cor do texto
        "success": (COLORS["successo_bg"], COLORS["successo"]), #sucesso
        "alert":   (COLORS["alerta_bg"],   COLORS["alerta"]), # alerta 
        "info":    (COLORS["financeiro_bg"], COLORS["financeiro"]),} # informação
    
    bg, fg = colors.get(color_key, (COLORS["card"], COLORS["text_primario"]))

    return ctk.CTkLabel(
        parent,
        text=f"  {text}  ",   
        font=("Segoe UI", 11, "bold"), # nome da fonte,tamanho e em negrito
        fg_color=bg,     #cor
        text_color=fg,   # cor do texto
        corner_radius=8, # borda arredondada
        **kwargs
    )