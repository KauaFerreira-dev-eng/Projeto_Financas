''' 
Pessoa 3: Davi
Ɛ> ════════════════════════════════════════════════════════ <3
                            To do
Ɛ> ════════════════════════════════════════════════════════ <3

--> (escreva oq desejar)
      oq desejar
(obs essa estrutura abaixo é obrigatória para o código funcionar)
'''

import customtkinter as ctk
from utils.theme import COLORS
from utils.widgets import Card, PrimaryButton, SectionTitle

class TodoView(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, fg_color="transparent")
        self._build()

    def _build(self):
        
        titulo = SectionTitle(self, "To-do List")
        titulo.pack(pady=20)
        
        card = Card(self)
        card.pack(fill="x", padx=20, pady=10)

        ctk.CTkLabel(card, text="Titulo").pack(anchor="w", padx=15, pady=(15,0))

        titulo_entry = ctk.CTkEntry(card)
        titulo_entry.pack(fill="x", padx=15, pady=5)

        ctk.CTkLabel(card, text="Descrição").pack(anchor="w", padx=15)

        descricao = ctk.CTkTextbox(card, height=80)
        descricao.pack(fill="x", padx=15, pady=5)

        prioridade = ctk.CTkOptionMenu(
            card,
            values=["Baixa","Média","Alta"]
        )

        prioridade.pack(padx=15, pady=5)

        prazo = ctk.CTkEntry(card,
                             placeholder_text="dd/mm/aaaa")
        
        prazo.pack(fill="x", padx=15, pady=5)

        btn = PrimaryButton(
            card,
            text="Adicionar tarefa"
        )

        btn.pack(pady=15)

        
        pass