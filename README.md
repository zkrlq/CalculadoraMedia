# 📚 Calculadora de Média Escolar

Aplicação desenvolvida em Python para realizar cálculos de média escolar de forma moderna, prática e intuitiva utilizando interface gráfica personalizada com **CustomTkinter**.

O projeto possui:

* Arquivo `.py` para estudos e edição do código
* Arquivo `.exe` para execução direta no Windows

---

# 📌 Tecnologias Utilizadas

* Python 3
* CustomTkinter
* Pandas
* Tkinter
* OpenPyXL

---

# 📂 Estrutura do Projeto

```bash id="lbyy2l"
calculadora-media/
│
├── CalculadoraMedia.py
├── CalculadoraMedia.exe
├── requirements.txt
└── README.md
```

---

# 🚀 Funcionalidades

* Cálculo automático da média escolar
* Sistema de aprovação e reprovação
* Interface moderna personalizada
* Barra de título customizada
* Salvamento automático em Excel (.xlsx)
* Seleção do local de salvamento
* Feedback visual colorido
* Tratamento de erros com `try` e `except`
* Execução em `.exe`
* Sistema de movimentação da janela

---

# 🖥️ Executável (.exe)

Caso não queira instalar Python, basta executar:

```bash id="t6wtxy"
CalculadoraMedia.exe
```

---

# 🐍 Executando pelo Python

## 1. Instale o Python

Download oficial:

https://www.python.org

---

## 2. Instale as dependências

```bash id="q0g5bq"
pip install customtkinter pandas openpyxl
```

---

## 3. Execute o projeto

```bash id="1w33wv"
python CalculadoraMedia.py
```

---

# 🧠 Como Funciona

O sistema permite:

1. Inserir o nome do aluno
2. Digitar as 4 notas bimestrais
3. Calcular automaticamente a média
4. Identificar aprovação ou reprovação
5. Salvar os resultados em uma planilha Excel

---

# 📐 Fórmula Utilizada

A média é calculada utilizando:

```text id="1z1zwj"
Média = (Nota1 + Nota2 + Nota3 + Nota4) ÷ 4
```

A fórmula matemática aplicada é:

\text{Média} = \frac{n_1 + n_2 + n_3 + n_4}{4}

---

# 📊 Salvamento em Excel

O sistema utiliza:

```python id="y3ay2d"
pandas.DataFrame()
```

para gerar automaticamente arquivos `.xlsx`.

As informações salvas incluem:

* Nome do aluno
* Todas as notas
* Média final
* Resultado final

---

# ⚠️ Tratamento de Erros

O projeto utiliza tratamento de exceções com:

```python id="27e1kd"
try:
```

e:

```python id="0vjlwm"
except:
```

---

## Erros Tratados

### Notas inválidas

```python id="86g4j8"
except ValueError:
```

### Erros ao salvar arquivos

```python id="94n9ot"
except Exception as e:
```

---

# 🎨 Interface

A interface foi construída utilizando:

```python id="vyg13w"
CustomTkinter
```

com:

* Tema claro
* Componentes modernos
* Botões personalizados
* Feedback visual em cores
* Barra de título personalizada

---

# 💡 Melhorias Futuras

* Tema escuro
* Histórico de alunos
* Sistema de recuperação
* Exportação para PDF
* Dashboard de desempenho
* Gráficos de notas
* Login de professores
* Banco de dados

---

# ✅ Boas Práticas Aplicadas

* Programação orientada a objetos (POO)
* Separação da lógica em métodos
* Interface organizada
* Tratamento de erros
* Salvamento seguro de arquivos
* Código modularizado

---

# 🔒 Observações

* O sistema salva os dados em formato `.xlsx`
* Recomendado utilizar Microsoft Excel ou LibreOffice
* Projeto voltado para fins educacionais

---

# 📸 Interface da Aplicação

```text id="yq1y1s"
+----------------------------------+
|        Média Escolar             |
|                                  |
| [ Nome do aluno              ]   |
| [ 1º Bimestre                ]   |
| [ 2º Bimestre                ]   |
| [ 3º Bimestre                ]   |
| [ 4º Bimestre                ]   |
|                                  |
|        [ Calcular ]              |
|      [ Salvar Média ]            |
|                                  |
|      Aprovado: 8.5               |
+----------------------------------+
```

---

# 👨‍💻 Autor

Projeto desenvolvido para estudos de:

* Python
* Interfaces gráficas
* Manipulação de arquivos Excel
* Programação orientada a objetos
* Tratamento de exceções

---

# ⭐ Contribuição

Contribuições são bem-vindas.

Faça um fork do projeto e envie um pull request.

---

# 📄 Licença

Este projeto está sob a licença MIT.
