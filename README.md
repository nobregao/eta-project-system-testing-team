# Projeto XYZ Bank  

## Visão Geral

Este repositório contém um projeto em Python para automatizar interações com um site bancário usando Selenium. O projeto está organizado em várias classes que representam diferentes páginas e funcionalidades do aplicativo bancário.

## Estrutura do Projeto

O projeto está organizado nos seguintes componentes principais:

1. **Pages**: Classes que representam diferentes páginas da aplicação, cada uma contendo métodos para interagir com os elementos dessa página.

2. **Model**: Contém a classe `Customer` representando informações do cliente.

3. **Tests**: Os testes estão organizados em diferentes classes de teste, cada uma focada em aspectos específicos da funcionalidade da aplicação.

4. **Fixtures**: Fixtures do Pytest são usadas para configurar cenários necessários para os testes.

## Como Executar os Testes

1. **Pré-requisitos**: Certifique-se de ter o Python e as dependências necessárias instaladas. Você pode instalar as dependências usando o arquivo `requirements.txt`.

   ```bash
   pip install -r requirements.txt
   
2. **Execução**:  Para executar os testes use o seguinte comando:

   ```bash
   pytest nome_do_arquivo.py

## Descrição dos Testes

1. **TestLoginCustomer**: Testa a funcionalidade de login para clientes.
2. **TestLoginManager**: Testa a funcionalidade de login para gerentes.
3. **TestCt1**: Adiciona um cliente e verifica a mensagem de sucesso.
4. **TestCt2**: Testa a criação bem-sucedida de uma conta de cliente.
5. **TestCt3**: Verifica se um cliente é adicionado à lista.
6. **TestCt4**: Testa a ordenação dos clientes em ordem alfabética.
7. **TestCt5**: Testa a funcionalidade de pesquisa para clientes.
8. **TestCt6**: Testa a exclusão de um cliente da lista.
9. **TestCt7**: Testa a realização de depósito na conta verificando saldo da conta
10. **TestCt8**: Testa o saque em uma conta de cliente
11. **TestCt9**: Verifica transação de depósito está no extrato de cliente

## Contribuidores

- [@andregabriele](https://github.com/andregabriele)
- [@nobregao](https://github.com/nobregao)
- [@rgutierress](https://github.com/rgutierress)
