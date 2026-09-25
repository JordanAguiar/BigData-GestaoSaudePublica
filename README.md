# BigData - Gestão de Saúde Pública

Sistema em Python para cadastro e consulta de pacientes vacinados, com uma etapa inicial de análise de dados (idade e distribuição de vacinas) usando Pandas e Matplotlib.

Projeto acadêmico com foco em manipulação de dados (CSV) e introdução a conceitos de análise de dados aplicados à saúde pública.

## Funcionalidades

O sistema (`Vacinacao.py`) apresenta um painel interativo via terminal com as opções:

1. **Criar Planilha** — gera o arquivo `registro.csv` com o cabeçalho (CPF, Nome, Idade, Data de Nascimento, Sexo, Vacina).
2. **Adicionar Paciente** — cadastra um novo paciente e a vacina aplicada (AstraZeneca, Pfizer ou CoronaVac).
3. **Verificar Pacientes** — lista todos os registros salvos.
4. **Consultar Paciente** — busca um paciente específico pelo CPF.
5. **Finalizar Programa** — encerra a execução.

Além disso, o script `AnaliseGrafica.py` faz uma análise exploratória inicial dos dados de `registro.csv`:

- 
- 
- 

> ⚠️ **Em desenvolvimento**

## Estrutura do projeto

```
BigData-GestaoSaudePublica/
├── Vacinacao.py         # Painel principal (menu do sistema)
├── funcoes.py           # Funções de cadastro, consulta e listagem de pacientes
├── AnaliseGrafica.py    # Análise exploratória e gráficos com Pandas/Matplotlib
├── registro.csv         # Base de dados dos pacientes (gerada/usada pelo sistema)
├── txt/
│   └── conteudos.txt    # Backup do conteúdo de registro.csv
└── requeriments.txt     # Dependências do projeto
```

## Tecnologias utilizadas

- Python 3
- [pandas](https://pandas.pydata.org/) — manipulação e análise dos dados
- [matplotlib](https://matplotlib.org/) — geração de gráficos
- Módulo `csv` da biblioteca padrão — leitura/escrita do registro de pacientes

## Como executar

1. Clone o repositório:

   ```bash
   git clone https://github.com/JordanAguiar/BigData-GestaoSaudePublica.git
   cd BigData-GestaoSaudePublica
   ```

2. Instale as dependências:

   ```bash
   pip install -r requeriments.txt
   ```

3. Para usar o sistema de cadastro de pacientes:

   ```bash
   python Vacinacao.py
   ```

4. Para rodar a análise exploratória dos dados:

   ```bash
   python AnaliseGrafica.py
   ```

## Autor

Desenvolvido por [Jordan Aguiar](https://github.com/JordanAguiar), [Alice Lima](https://github.com/alice-estudante) e [Igor Lyra](https://github.com/Igotkun)  

