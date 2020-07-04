# Automações de rotinas de jogos da loteria.

## Automação de conferencia da Lotofácil - Loterias da Caixa

Essa aplicação foi criada com objetivo de aprendizado do básico da linguagem python, com automatização de tarefas repetitivas, lançando mão de bibliotecas como selenium para realizar as capturas nos sites de resultados de loterias caixa e automatizar o processo de conferência dos número apostados.

A principio foi construído uma aplicação console para ao invocar as linhas de comando, conforme as instruções nos tópicos mais abaixo. Ela permite cadastrar apostas e realizar a conferencia dos resultados buscados de forma online nos sites oficiais.

É uma aplicação na qual tento explorar alguns conceitos de orientação a objeto, alguns patterns do DDD como por exemplo o pattern Repository utilizando um banco em arquivo binário com a biblioteca Shelve.

A ferramenta como aprendizado foi muito importante, mas apenas um passo inicial, sigo no meu objetivo de aprender a linguagem python e suas principais bibliotecas, com objetivos profissionais e pessoais, pois entendi que ela pode contribuír com a automatização de procedimentos rotineiros do dia a dia, eliminando tarefas repetitivas e ganhando eficiência em qualquer objetivo no qual me coloque a serviço.

O código está disponível para aprendizado, colaborações e como parte de um começo na construção de portifólio.

Há enumeros problemas também e simplificações, mas como ponta pé inicial fico satisfeito na publicação e compartilhamento.

## Tecnologias:

- Python 3
- Principais Bibliotecas:
    - Selenium (Capturar e navegar em páginas da web)
    - Shelve (Como armazenamento de Banco de dados em arquivo binário)
    - Sys (lidar com linha de comando e passagem de argumentos)
    - json (serializar objetos)
    

## Pré requisitos

- Python 3

- Instalar o driver do selenium, no código o driver foi apontado para o diretório C:\\geckodriver.exe

Referência que foi importante para essa configuração:
https://link.medium.com/xqoeRlDHQ7 


## Instruções

Nessa primeira versão existe apenas conferencia de jogo da lotofácil.

- Cadastrar novas apostas 

```python betcheck.py adicionar```

- Listar as apostas Cadastradas

```
python betcheck.py listar
```

- Listar os concursos

python betcheck.py listar-concurso

- Conferir resultados 

``` 
python betcheck.py conferir
```