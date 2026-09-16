[KEDA](https://github.com/user-attachments/files/32312147/README.1.md)
# Organizador Pessoal Inteligente

Um aplicativo desktop de organização pessoal, desenvolvido em **Python** com **CustomTkinter**, que reúne em um só lugar controle financeiro, lista de tarefas, calendário de eventos e um cronômetro Pomodoro para gestão de foco e produtividade.

Projeto desenvolvido na disciplina de **Introdução a Python**, do curso de **Análise e Desenvolvimento de Sistemas da UEPB**.

O app leva o nome **KEDA**, sigla para **"Keep Every Day Aligned"**, formada também a partir das iniciais dos nomes dos autores: **K**auã, **E**ugênio, **D**avi e **A**na Luiza.

## Funcionalidades

- **Início** — Painel inicial com um resumo geral das outras áreas do app.
- **Financeiro** — Registro de transações (entradas e saídas), cálculo automático de saldo e exportação/importação de dados em CSV.
- **To-do List** — Criação, marcação de conclusão e exclusão de tarefas, com persistência dos dados salvos localmente.
- **Calendário** — Visualização mensal com cadastro de eventos por data.
- **Pomodoro** — Criação de sessões de estudo/foco personalizadas (tempo de foco, pausa curta, pausa longa e número de ciclos), com cronômetro dedicado e histórico de sessões realizadas.
- **Tema claro/escuro** — Interface personalizável com paleta de cores centralizada.

## Tecnologias utilizadas

- [Python 3](https://www.python.org/)
- [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) — biblioteca de interface gráfica
- [Pillow (PIL)](https://python-pillow.org/) — manipulação de imagens/ícones
- Módulos padrão do Python: `json`, `os`, `csv`, `datetime`, `calendar`, `tkinter`

Os dados de cada módulo (tarefas, transações, eventos e sessões de pomodoro) são persistidos localmente em arquivos `.json` na pasta `data/`.

## 📁 Estrutura do projeto

```
organizador/
├── main.py                  # Ponto de entrada da aplicação
├── data/                     # Armazenamento local dos dados (JSON)
│   ├── calendario.json
│   ├── financeiro.json
│   ├── pomodoro.json
│   └── todo.json
├── icons/                    # Ícones utilizados na interface
├── utils/
│   ├── theme.py               # Paleta de cores do app
│   └── widgets.py              # Componentes visuais reutilizáveis (cards, botões etc.)
└── views/
    ├── home.py                 # Tela inicial
    ├── financeiro.py            # Tela de controle financeiro
    ├── todo.py                  # Tela de lista de tarefas
    ├── calendario.py            # Tela de calendário
    ├── pomodoro.py               # Tela de gerenciamento de sessões Pomodoro
    ├── pomodoro_dados.py          # Modelo e persistência das sessões Pomodoro
    └── pomodoro_timer.py           # Cronômetro do Pomodoro
```

## ▶️ Como executar

1. Certifique-se de ter o **Python 3** instalado.
2. Instale as dependências necessárias:
   ```bash
   pip install customtkinter pillow
   ```
3. Navegue até a pasta `organizador` e execute o arquivo principal:
   ```bash
   cd organizador
   python main.py
   ```

## 👥 Autores

- Kauã Ferreira
- Eugênio Genuíno Mota
- Davi Marinho Donato
- Ana Luiza Almeida Maia

## 📄 Licença

Projeto desenvolvido para fins acadêmicos/estudo.
