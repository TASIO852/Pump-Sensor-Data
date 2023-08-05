# Documentação Completa do Desafio Técnico

## 1. **Serviço de Solicitação de Dados (API GET)**

### a. **Leitura e Filtragem de Dados**

- **Arquivo:** `data_handler.py`
- **Funções:** Para ler o arquivo, filtrar dados de acordo com os critérios do desafio (abril de 2018, sensores 07 e 47, valores entre 20 e 30), e preparar a resposta.

### b. **API GET**

- **Metodologia:** Responder com os dados filtrados em formato JSON via GET request e exibe na interface (A rota esta na no arquivo `routes.py`).

## 2. **Serviço de Recepção de Dados (API POST)**

### a. **Recepção de Dados**

- **Arquivo:** `data_handler.py`
- **Funções:** Para enviar os dados via POST para o diretorio DATA simulando um BD que passam por um `validador.py` e depois são organizadas e apos e criado um arquivo CSV com os dados

### b. **Organização de Dados**

- **Processamento:** Organizar os dados em um Pandas DataFrame com colunas específicas (Data, Hora, Sensor, Medição, Status), e exibi-lo no console (A rota esta na no arquivo `routes.py`).

## 3. **Interface de Usuário Avançada ╰(*°▽°*)╯**

### a. **Interface da Chamada de API**

- Estrutura HTML com cabeçalho, corpo, botões, e tabela de resultados.
- JavaScript/jQuery com funções e manipuladores de eventos de front-end.
- Estilização com CSS.

### b. **HTML Resultados**

- Painel de controle com botões POST,GET e tabela para apresentar os dados do GET.
- Estilização com arquivo CSS separado.

## 4. **Estrutura de Pastas**

- **Organização:** Arquivos organizados de forma clara, facilitando a execução e manutenção como na estrutura de pastas abaixo.

```
Pump Sensor Data
├─ app
│  ├─ static
│  │  └─ css
│  │     └─ styles.css
│  ├─ templates
│  │  └─ index.html
│  ├─ validator.py
│  ├─ config.py
│  ├─ data_handler.py
│  ├─ routes.py
│  └─ __init__.py
├─ data
│   └─ pump_sensor_data.csv
├─ docs
│   └─ Prueba Técnica Desarrollador Python Semi SR _ ENGLISH.pdf
├─ tests
│   └─ test.py
├─ .gitignore
├─ main.py
├─ README.md
├─ requirements.txt
 
```

## 5. **Instruções de Instalação e execução**

- **Pre-config:** No arquivo `config.py` coloque os caminhos que tem seu computador para que o codigo funcione
- **Dependências:** Lista de todas as bibliotecas necessárias no arquivo `requirements.txt`, para instalação via PIP.
- **Execução:** Depois de tudo instalado executo o arquivo `main.py` e no seu browser entre no`"http://localhost:5000` e divirta-se (❁´◡`❁).

## Conclusão

Esta documentação abrange tanto o desafio técnico quanto componentes adicionais desenvolvidos para se destacar. O foco principal permanece no desenvolvimento das APIs para consulta e carregamento de dados, mas também inclui uma interface de usuário avançada com HTML, JavaScript/jQuery, e CSS. Esses extras demonstram uma abordagem mais complexa e completa, oferecendo funcionalidades adicionais que vão além do desafio proposto.
