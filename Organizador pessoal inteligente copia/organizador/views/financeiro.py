''' 
Pessoa 2: Kaua 
Ɛ> ════════════════════════════════════════════════════════ <3
                            Financeiro
Ɛ> ════════════════════════════════════════════════════════ <3

--> (escreva oq desejar)

(obs essa estrutura abaixo é obrigatória para o código funcionar)
'''

import customtkinter as ctk

from utils.theme import COLORS
from utils.widgets import (
    Card,
    PrimaryButton,
    SecondaryButton,
    SectionTitle,
    MutedLabel,
    Badge
)


class FinanceiroView(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, fg_color="transparent")

        self.transacoes = []
        self.saldo = 0.0

        self._build()
        self._atualizar_resumo()

    def _build(self):
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=2)
        self.grid_rowconfigure(1, weight=1)

        self._build_resumo()
        self._build_formulario()
        self._build_lista()

    def _build_resumo(self):
        frame = ctk.CTkFrame(self, fg_color="transparent")
        frame.grid(row=0, column=0, columnspan=2, sticky="ew", pady=(0, 15))

        frame.grid_columnconfigure((0, 1, 2), weight=1)

        self.card_saldo = Card(frame)
        self.card_saldo.grid(row=0, column=0, padx=5, sticky="ew")

        SectionTitle(
            self.card_saldo,
            "💰 Saldo Total"
        ).pack(pady=(10, 5))

        self.label_saldo = ctk.CTkLabel(
            self.card_saldo,
            text="R$ 0,00",
            font=("Segoe UI", 24, "bold")
        )
        self.label_saldo.pack(pady=(0, 10))

        self.card_receitas = Card(
            frame,
            fg_color=COLORS["successo_bg"]
        )
        self.card_receitas.grid(
            row=0,
            column=1,
            padx=5,
            sticky="ew"
        )

        SectionTitle(
            self.card_receitas,
            "📈 Receitas"
        ).pack(pady=(10, 5))

        self.label_receitas = ctk.CTkLabel(
            self.card_receitas,
            text="R$ 0,00",
            font=("Segoe UI", 22, "bold"),
            text_color=COLORS["successo"]
        )
        self.label_receitas.pack(pady=(0, 10))

        self.card_despesas = Card(
            frame,
            fg_color=COLORS["alerta_bg"]
        )
        self.card_despesas.grid(
            row=0,
            column=2,
            padx=5,
            sticky="ew"
        )

        SectionTitle(
            self.card_despesas,
            "📉 Despesas"
        ).pack(pady=(10, 5))

        self.label_despesas = ctk.CTkLabel(
            self.card_despesas,
            text="R$ 0,00",
            font=("Segoe UI", 22, "bold"),
            text_color=COLORS["alerta"]
        )
        self.label_despesas.pack(pady=(0, 10))

    def _build_formulario(self):
        form = Card(self)
        form.grid(
            row=1,
            column=0,
            sticky="nsew",
            padx=(0, 10)
        )

        form.grid_columnconfigure(0, weight=1)

        SectionTitle(
            form,
            "Nova Transação"
        ).grid(
            row=0,
            column=0,
            padx=15,
            pady=15,
            sticky="w"
        )

        self.tipo_var = ctk.StringVar(
            value="receita"
        )

        ctk.CTkRadioButton(
            form,
            text="Receita",
            variable=self.tipo_var,
            value="receita"
        ).grid(
            row=1,
            column=0,
            padx=15,
            sticky="w"
        )

        ctk.CTkRadioButton(
            form,
            text="Despesa",
            variable=self.tipo_var,
            value="despesa"
        ).grid(
            row=2,
            column=0,
            padx=15,
            pady=(5, 10),
            sticky="w"
        )

        self.desc_entry = ctk.CTkEntry(
            form,
            placeholder_text="Descrição"
        )
        self.desc_entry.grid(
            row=3,
            column=0,
            padx=15,
            pady=5,
            sticky="ew"
        )
        
        self.valor_entry = ctk.CTkEntry(
            form,
            placeholder_text="Valor"
        )
        self.valor_entry.grid(
            row=4,
            column=0,
            padx=15,
            pady=5,
            sticky="ew"
        )

        ctk.CTkLabel(form, text="Categoria").grid(
            row=5, column=0, padx=15, sticky="w"
        )

        self.categoria_var = ctk.StringVar(value="Alimentação")

        self.categoria_entry = ctk.CTkComboBox(
            form,
            values=[
                "Alimentação",
                "Transporte",
                "Moradia",
                "Saúde",
                "Educação",
                "Lazer",
                "Salário",
                "Freelance",
                "Outros"
            ],
            variable=self.categoria_var
        )
        self.categoria_entry.grid(
            row=6, column=0, padx=15, pady=5, sticky="ew"
        )

        PrimaryButton(
            form,
            text="Adicionar",
            command=self._adicionar_transacao
        ).grid(
            row=7,
            column=0,
            padx=15,
            pady=(15, 5),
            sticky="ew"
        )

        SecondaryButton(
            form,
            text="Limpar",
            command=self._limpar_campos
        ).grid(
            row=8,
            column=0,
            padx=15,
            pady=(0, 5),
            sticky="ew"
        )

        SecondaryButton(
            form,
            text="🗑 Limpar Histórico",
            command=self._limpar_historico
        ).grid(
            row=9,
            column=0,
            padx=15,
            pady=(0, 15),
            sticky="ew"
        )

    def _build_lista(self):
        lista = Card(self)
        lista.grid(
            row=1,
            column=1,
            sticky="nsew"
        )

        lista.grid_rowconfigure(1, weight=1)
        lista.grid_columnconfigure(0, weight=1)

        SectionTitle(
            lista,
            "Histórico"
        ).grid(
            row=0,
            column=0,
            padx=15,
            pady=15,
            sticky="w"
        )

        self.lista_scroll = ctk.CTkScrollableFrame(
            lista
        )
        self.lista_scroll.grid(
            row=1,
            column=0,
            padx=10,
            pady=(0, 10),
            sticky="nsew"
        )

        self.label_vazio = MutedLabel(
            self.lista_scroll,
            text="Nenhuma transação cadastrada."
        )
        self.label_vazio.pack(pady=20)

    def _adicionar_transacao(self):
        descricao = self.desc_entry.get().strip()

        try:
            valor = float(
                self.valor_entry.get().replace(",", ".")
            )
        except:
            self._mostrar_erro(
                "Digite um valor válido."
            )
            return

        if descricao == "":
            self._mostrar_erro(
                "Digite uma descrição."
            )
            return

        self.transacoes.append({
            "descricao": descricao,
            "valor": valor,
            "tipo": self.tipo_var.get(),
            "categoria": self.categoria_var.get()
        })

        self._renderizar_lista()
        self._atualizar_resumo()
        self._limpar_campos()

    def _renderizar_lista(self):
        for widget in self.lista_scroll.winfo_children():
            widget.destroy()

        if not self.transacoes:
            self.label_vazio = MutedLabel(
                self.lista_scroll,
                text="Nenhuma transação cadastrada."
            )
            self.label_vazio.pack(pady=20)
            return

        for transacao in reversed(self.transacoes):
            cor = (
                COLORS["successo"]
                if transacao["tipo"] == "receita"
                else COLORS["alerta"]
            )

            texto_tipo = (
                "Receita"
                if transacao["tipo"] == "receita"
                else "Despesa"
            )

            item = Card(self.lista_scroll)
            item.pack(
                fill="x",
                padx=5,
                pady=5
            )

            ctk.CTkLabel(
                item,
                text=transacao["descricao"],
                anchor="w"
            ).pack(
                side="left",
                padx=10
            )

            Badge(
                item,
                texto_tipo,
                color_key=(
                    "success"
                    if transacao["tipo"] == "receita"
                    else "alert"
                )
            ).pack(
                side="right",
                padx=10
            )

            ctk.CTkLabel(
                item,
                text=f"R$ {transacao['valor']:.2f}",
                text_color=cor,
                font=("Segoe UI", 12, "bold")
            ).pack(
                side="right",
                padx=10
            )

            btn_excluir = ctk.CTkButton(
                item,
                text="✖",
                width=30,
                height=30,
                fg_color="transparent",
                text_color=COLORS["alerta"],
                hover_color=COLORS["alerta_bg"],
                command=lambda t=transacao: self._excluir_transacao(t)
            )
            btn_excluir.pack(side="right", padx=5)

    def _excluir_transacao(self, transacao):
        if transacao in self.transacoes:
            self.transacoes.remove(transacao)

        self._renderizar_lista()
        self._atualizar_resumo()

    def _limpar_historico(self):
        self.transacoes.clear()
        self._renderizar_lista()
        self._atualizar_resumo()

    def _atualizar_resumo(self):
        receitas = sum(
            t["valor"]
            for t in self.transacoes
            if t["tipo"] == "receita"
        )

        despesas = sum(
            t["valor"]
            for t in self.transacoes
            if t["tipo"] == "despesa"
        )

        saldo = receitas - despesas

        self.label_saldo.configure(
            text=f"R$ {saldo:.2f}"
        )

        self.label_receitas.configure(
            text=f"R$ {receitas:.2f}"
        )

        self.label_despesas.configure(
            text=f"R$ {despesas:.2f}"
        )

    def _limpar_campos(self):
        self.desc_entry.delete(0, "end")
        self.valor_entry.delete(0, "end")
        self.tipo_var.set("receita")

    def _mostrar_erro(self, mensagem):
        janela = ctk.CTkToplevel(self)
        janela.title("Erro")
        janela.geometry("300x150")
        janela.transient(self)
        janela.grab_set()

        ctk.CTkLabel(
            janela,
            text=mensagem
        ).pack(pady=25)

        PrimaryButton(
            janela,
            text="OK",
            command=janela.destroy
        ).pack(pady=10)
