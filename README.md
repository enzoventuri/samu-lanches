
# 🍔 Sistema de Lanchonete Delivery

**Projeto de Programação Orientada a Objetos – SENAI**

## 📌 Sobre o Projeto

O Sistema de Lanchonete Delivery é um projeto desenvolvido em Python com o objetivo de organizar e gerenciar os produtos de uma lanchonete.

O sistema funciona pelo terminal e permite cadastrar, listar, buscar e preparar diferentes tipos de produtos, utilizando os conceitos fundamentais da Programação Orientada a Objetos (POO).

O projeto foi desenvolvido como atividade prática do SENAI, utilizando Python, PyCharm, Git e GitHub.

## 👥 Integrantes

- Enzo Venturi
- Samuel Friedrichsen
- Lucca Reck
- Carlos Barreto

**Turma:** 2922

## 🎯 Objetivos do Sistema

- Cadastrar lanches, bebidas e sobremesas.
- Listar todos os produtos cadastrados.
- Buscar produtos pelo nome.
- Simular a preparação dos produtos.
- Aplicar encapsulamento, herança e polimorfismo.
- Praticar o versionamento colaborativo com Git e GitHub.

## 🛠️ Tecnologias Utilizadas

- Python 3
- PyCharm
- Git
- GitHub

## 📂 Estrutura do Projeto

```text
Lanchonete/
│
├── main.py
├── Produto.py
├── Lanche.py
├── Lanchonete.py
├── Bebida.py
├── Sobremesa.py
├── README.md
└── .gitignore
```

## 🧩 Descrição das Classes

### 1. Produto (Classe Base)

Representa um produto genérico da lanchonete.

**Atributos:**
- Nome
- Preço
- Quantidade em estoque

**Métodos:**
- Getters e setters com validação.
- `calcular_preco_final()`
- `preparar()`
- `__str__()`

### 2. Lanche (Classe Filha)

Representa os lanches vendidos pela lanchonete.

**Atributos próprios:**
- Tipo de pão
- Ingredientes

**Métodos próprios:**
- `adicionar_ingrediente()`
- `preparar()`
- `__str__()`

### 3. Bebida (Classe Filha)

Representa as bebidas disponíveis para delivery.

**Atributos próprios:**
- Tamanho em mililitros
- Estado térmico (gelada ou não)

**Métodos próprios:**
- `servir_com_gelo()`
- `preparar()`
- `__str__()`

### 4. Sobremesa (Classe Filha)

Representa as sobremesas comercializadas pela lanchonete.

**Atributos próprios:**
- Temperatura
- Calorias
- Cobertura extra

**Métodos próprios:**
- `adicionar_cobertura()`
- `eh_diet()`
- `preparar()`
- `__str__()`

### 5. Lanchonete (Classe Gerenciadora)

Responsável por administrar os produtos cadastrados.

Está implementada no arquivo `main.py`.

**Responsabilidades:**
- Armazenar os produtos em uma lista privada.
- Cadastrar produtos.
- Listar produtos.
- Buscar produtos pelo nome.
- Executar a preparação dos produtos.

## 📊 Diagrama de Classes

```text
                 ┌──────────────────┐
                 │     Produto      │
                 ├──────────────────┤
                 │ - __nome         │
                 │ - __preco        │
                 │ - __quantidade   │
                 ├──────────────────┤
                 │ + preparar()     │
                 │ + __str__()      │
                 └────────┬─────────┘
                          │
              ┌───────────┼───────────┐
              │           │           │
       ┌──────▼────┐ ┌────▼─────┐ ┌───▼────────┐
       │   Lanche  │ │  Bebida  │ │ Sobremesa  │
       ├───────────┤ ├──────────┤ ├────────────┤
       │ - __pao   │ │ - _tamanho│ │ - __temperatura
       │ - _ingred.│ │ - _gelada │ │ - __calorias
       ├───────────┤ ├──────────┤ ├────────────┤
       │ + preparar│ │ + preparar│ │ + preparar │
       └───────────┘ └──────────┘ └────────────┘

                 ┌──────────────────┐
                 │    Lanchonete    │
                 ├──────────────────┤
                 │ - __produtos     │
                 ├──────────────────┤
                 │ + cadastrar()    │
                 │ + listar()       │
                 │ + buscar()       │
                 │ + preparar()     │
                 └──────────────────┘
```

## 🧠 Conceitos de POO Aplicados

### Encapsulamento

Os atributos são protegidos ou privados, utilizando propriedades (`@property`), getters e setters para controlar o acesso e validar os dados.

Exemplos de validações:
- O nome do produto não pode ser vazio.
- O preço deve ser maior que zero.
- O volume da bebida deve ser positivo.
- A quantidade de calorias deve ser válida.

### Herança

As classes Lanche, Bebida e Sobremesa herdam os atributos e métodos da classe Produto.

A utilização de `super().__init__()` permite reaproveitar o construtor da classe base.

### Polimorfismo

As classes filhas sobrescrevem o método `preparar()`.

Dessa maneira, cada tipo de produto apresenta um comportamento diferente quando o sistema percorre a lista de produtos e executa o mesmo método.

## 💻 Funcionalidades do Menu

O sistema apresenta as seguintes opções:

| Opção | Funcionalidade |
|---|---|
| 1 | Cadastrar produto |
| 2 | Listar produtos |
| 3 | Buscar produto |
| 4 | Preparar produtos |
| 0 | Sair do sistema |

O menu permanece ativo até o usuário escolher a opção de saída.

O sistema também possui tratamento de erros para entradas inválidas e validações dos dados informados.

## ▶️ Como Executar o Projeto

**1.** Instale o Python 3 em seu computador.

**2.** Clone o repositório:

```bash
git clone URL_DO_REPOSITORIO
```

**3.** Abra a pasta do projeto no PyCharm.

**4.** Verifique se todos os arquivos estão na mesma pasta.

**5.** Execute o arquivo `main.py`.

```bash
python main.py
```

**6.** Utilize o menu apresentado no terminal para interagir com o sistema.

## 🔀 Versionamento com Git e GitHub

O desenvolvimento do projeto é realizado de forma colaborativa utilizando Git e GitHub.

Todos os integrantes participam do desenvolvimento por meio de commits individuais na branch `main`.

Fluxo de trabalho utilizado:

```bash
git pull
git add .
git commit -m "Descrição da alteração"
git push
```

O arquivo `.gitignore` é utilizado para evitar o envio de arquivos desnecessários, como:

- `__pycache__/`
- `.idea/`
- 
## 📚 Aprendizados

Durante o desenvolvimento do projeto, foram trabalhados conceitos importantes de programação, como:

- Criação e organização de classes e objetos.
- Encapsulamento e validação de atributos.
- Herança e reutilização de código.
- Polimorfismo e sobrescrita de métodos.
- Manipulação de listas e estruturas de repetição.
- Entrada e saída de dados pelo terminal.
- Tratamento de exceções.
- Versionamento e colaboração utilizando Git e GitHub.

