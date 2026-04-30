# Projeto Biblioteca - INF1407

## Alunos

* Lucie Brunelle
* Théo Lemaire

---

## Escopo do Projeto

Este projeto consiste em um sistema web de gerenciamento de biblioteca pessoal, desenvolvido para a disciplina de Programação para Web.

O objetivo principal é permitir que usuários gerenciem seu próprio catálogo de livros através de uma interface simples, intuitiva e responsiva.

---

## Funcionalidades Implementadas

### Sistema de Autenticação

* Cadastro de novos usuários (register)
* Login e logout
* Recuperação de senha (fluxo por e-mail simulado)

### Gestão de Livros (CRUD)

* Criar (adicionar novos livros)
* Ler (visualizar lista e detalhes)
* Atualizar (editar informações)
* Deletar (remover livros)

### Gestão por Usuário

* Cada usuário gerencia apenas seus próprios livros
* Interface adaptada para usuários autenticados

### Visualização

* Página inicial com lista de livros
* Página de detalhe para cada livro

### Interface

* Design responsivo
* Desenvolvido apenas com HTML e CSS (sem JavaScript)

---

## Tecnologias Utilizadas

* **Backend:** Python 3.x + Django 5.x
* **Frontend:** HTML5 + CSS3
* **Banco de Dados:** SQLite
* **Servidor:** Render
* **Controle de versão:** Git + GitHub

---

## O que funcionou

* Sistema completo de autenticação
* CRUD completo dos livros
* Separação de livros por usuário
* Página de detalhes dos livros
* Deploy funcional na plataforma Render
* Interface responsiva e navegável

---

## O que não funcionou

* Sistema de envio real de e-mails (apenas simulado no console)
* Algumas limitações relacionadas ao banco SQLite em produção

---

## Como usar

###  Acessar o site

Acesse:
https://inf1407-prog-web.onrender.com

---

###  Criar uma conta

* Acesse `/register/`
* Preencha usuário e senha
* O login é feito automaticamente após cadastro

---

###  Fazer login

* Acesse `/accounts/login/`
* Insira suas credenciais
* Clique em "Entrar"

---

###  Recuperar senha

* Clique em "Esqueceu sua senha?"
* Siga as instruções exibidas (simuladas)

---

###  Gerenciar livros

####  Adicionar livro

* Clique em "Adicionar livro"
* Preencha título, autor e descrição

####  Editar livro

* Disponível apenas para o dono do livro

####  Deletar livro

* Disponível apenas para o dono do livro

####  Ver detalhes

* Clique em qualquer livro da lista

---

## Possíveis melhorias futuras

*  Sistema de avaliações (reviews) para livros
*  Upload de imagem de capa dos livros
*  Sistema de busca e filtros
*  Classificação por categorias ou gêneros
*  Compartilhamento de livros entre usuários
*  Melhorias na interface responsiva

---

## Observações

O projeto foi desenvolvido respeitando as restrições da disciplina:

* Sem uso de JavaScript
* Uso obrigatório de Django
* Implementação de CRUD completo
* Sistema de usuários com permissões

---

##  Conclusão

O sistema atende aos requisitos propostos, oferecendo uma solução funcional e organizada para gerenciamento de biblioteca pessoal, com possibilidade de expansão futura.
