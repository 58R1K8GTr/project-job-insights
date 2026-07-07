# 📈 Job Insights — Análise de Dados e Manipulação de Arquivos com Python

O **Job Insights** é uma aplicação focada na extração, tratamento e análise de dados sobre o mercado de trabalho, utilizando um conjunto de dados reais extraídos do Glassdoor (via Kaggle). O objetivo principal deste projeto foi desenvolver ferramentas de mineração e filtragem de dados brutos armazenados em arquivos CSV, aplicando conceitos fundamentais de **Ciência da Computação** com **Python**.

A arquitetura do projeto foi estruturada utilizando Programação Orientada a Objetos (POO) e herança para criar módulos especializados em analisar tipos de empregos, setores industriais e faixas salariais.

---

## 🚀 Habilidades Desenvolvidas & Consolidadas

Este projeto marcou a consolidação de fundamentos essenciais de engenharia de software e manipulação de dados em Python:

* **Manipulação Avançada de Arquivos (I/O):**
    * Leitura estruturada de arquivos de dados volumosos (`.csv`) e conversão dinâmica para estruturas nativas do Python (lista de dicionários), mapeando cabeçalhos como chaves.
* **Lógica de Programação & Algoritmos de Filtragem:**
    * Uso eficiente de estruturas condicionais, compreensões de lista (*List Comprehensions*) e estruturas de repetição para filtragem multicritério e identificação de valores únicos.
* **Tratamento de Exceções e Robustez:**
    * Implementação rigorosa de validação de dados com lançamentos de exceções nativas (`ValueError` e `TypeError`) para blindar o sistema contra payloads inválidos, dados ausentes ou tipos corrompidos.
* **Programação Orientada a Objetos (POO):**
    * Utilização de herança onde subclasses (`ProcessSalaries`, `ProcessIndustries`) herdam o estado e os métodos de leitura da classe base (`ProcessJobs`), evitando redundância de I/O no disco.
* **Testes Automatizados com Pytest:**
    * Escrita de testes utilizando o framework **Pytest** para validar comportamentos complexos, incluindo testes *case-insensitive* e garantia de lançamentos de erros (*XFAIL* / asserções de exceções).
* **Qualidade de Código & Clean Code:**
    * Garantia de conformidade estilística com as normas da **PEP 8** utilizando o linter **Flake8** para manter o código altamente legível e manutenível.

---

## 📁 Estrutura de Módulos e Insights Implementados

O projeto foi dividido em submódulos de análise contidos no pacote `insights`:

1.  **Módulo de Empregos (`jobs.py`):** Responsável por carregar o arquivo em memória, extrair a listagem de tipos de vagas existentes e realizar filtragens dinâmicas por múltiplos critérios.
2.  **Módulo de Indústrias (`industries.py`):** Focado no agrupamento e isolamento dos setores industriais mapeados no mercado de trabalho.
3.  **Módulo de Salários (`salaries.py`):** Responsável por minerar as faixas salariais, descobrindo tetos (`max_salary`) e pisos (`min_salary`), além de validar se o salário de uma vaga atende a determinados intervalos de busca.

---

## 🛠️ Tecnologias e Ferramentas Utilizadas

* **Linguagem Principal:** Python 3 (v3.8+)
* **Framework de Testes:** Pytest
* **Linter de Estilo:** Flake8
* **Ambiente Isolado:** Virtualenv (`.venv`)

---

## 🏕️ Configuração do Ambiente e Execução

O projeto faz o gerenciamento de suas dependências por meio de ambientes virtuais isolados.

### 1. Preparando o Ambiente Virtual

```bash
# Criar o ambiente virtual (.venv)
python3 -m venv .venv

# Ativar o ambiente virtual
source .venv/bin/activate

# Instalar as dependências de desenvolvimento
python3 -m pip install -r dev-requirements.txt
```

### 2. Executando os Testes Automatizados
Com o ambiente virtual ativo, você pode rodar e auditar os testes de diversas formas:

```bash
python3 -m pytest
python3 -m pytest -s -vv
python3 -m pytest -x
```

### 3. Verificando a qualidade de código (linter)
Para garantir que o código cumpre as diretrizes formais da PEP 8, execute o comando:

```bash
python3 -m flake8
```

## 📐 Estrutura de Arquivos Modificados
A organização modular do repositório garante a separação entre dados, código de produção e testes de qualidade:

```text
├── data/
│   └── jobs.csv               # Massa de dados brutos sobre empregos
├── src/
│   └── insights/
│       ├── industries.py      # Filtros e mapeamento de indústrias
│       ├── jobs.py            # Classe base de processamento e leitura do CSV
│       └── salaries.py        # Validação e mineração de faixas salariais
└── tests/
    ├── brazilian/             # Testes de tradução de relatórios
    └── counter/               # Testes de contagem de termos específicos
```
