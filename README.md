# Projeto Biblioteca - INF1407

## Alunos
* **Lucie Brunelle**
* **Théo Lemaire**

## Escopo do Projeto
Este projeto é um sistema de gerenciamento de biblioteca desenvolvido para a disciplina de Programação para Web. O objetivo principal é permitir que usuários gerenciem seu catálogo pessoal de livros através de uma interface web simples e funcional.

**Funcionalidades principais implementadas:**
* **Sistema de Autenticação Completo:** Cadastro de novos usuários, login, logout e fluxo de recuperação de senha por e-mail (simulado via console).
* **Gestão de Livros (CRUD):** Possibilidade de listar, adicionar, editar e excluir livros do banco de dados.
* **Interface Responsiva:** Design limpo utilizando CSS puro, sem o uso de frameworks externos ou JavaScript, conforme as restrições do trabalho.
* **Visões Personalizadas:** Diferenciação de interface para usuários logados e visitantes.

## Tecnologias Utilizadas
* **Backend:** Python 3.x + Django 6.x
* **Frontend:** HTML5 e CSS3
* **Banco de Dados:** SQLite (padrão do Django para desenvolvimento)
* **Controle de Versão:** Git

## O que funcionou


## O que nao funcionou


## Como usar
* Criar uma conta : Acesse /register/, coloque um nome de usuário e senha e clique em Cadastrar. Você já fica logado automaticamente.
* Fazer login : Acesse /accounts/login/, coloque seu usuário e senha e clique em Entrar.
  Se esquecer a senha, clique em "Esqueceu sua senha?" e siga as instruções por email.
* Ver os livros : A página inicial mostra todos os livros cadastrados. Clique em qualquer livro para ver os detalhes.
* Adicionar um livro : Estando logado, clique em "Adicionar livro", preencha o título, autor e descrição, e salve.
* Editar um livro : Na lista ou na página do livro, clique em "Editar". Esse botão só aparece para o dono do livro.
* Deletar um livro : Na lista ou na página do livro, clique em "Deletar". Só o dono pode fazer isso.

