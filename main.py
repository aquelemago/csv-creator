# -*- coding: utf-8 -*-
import os
import csv
import random
from datetime import datetime, timedelta

# --- Funções para Gerar os Datasets ---

def criar_diretorio_se_nao_existir():
    """Verifica se a pasta 'output' existe, senão a cria."""
    if not os.path.exists('output'):
        os.makedirs('output')

def gerar_dataset_vendas(linhas):
    """Gera um arquivo CSV de vendas."""
    criar_diretorio_se_nao_existir()
    
    # Abre o arquivo para escrita
    with open('output/vendas.csv', 'w', newline='', encoding='utf-8') as arquivo_csv:
        escritor = csv.writer(arquivo_csv)
        
        # Escreve o cabeçalho
        escritor.writerow(['Vendas', 'Lucro', 'Região', 'Data', 'Cliente', 'Produto'])
        
        # Gera e escreve as linhas de dados
        for _ in range(linhas):
            vendas = round(random.uniform(100, 10000), 2)
            lucro = round(vendas * random.uniform(0.1, 0.4), 2)
            regiao = random.choice(['Norte', 'Sul', 'Leste', 'Oeste'])
            data = (datetime.now() - timedelta(days=random.randint(0, 365))).strftime('%Y-%m-%d')
            cliente = f'Cliente {random.randint(1, 100)}'
            produto = f'Produto {random.randint(1, 20)}'
            
            escritor.writerow([vendas, lucro, regiao, data, cliente, produto])

def gerar_dataset_rh(linhas):
    """Gera um arquivo CSV de RH."""
    criar_diretorio_se_nao_existir()
    
    with open('output/rh.csv', 'w', newline='', encoding='utf-8') as arquivo_csv:
        escritor = csv.writer(arquivo_csv)
        
        # Cabeçalho
        escritor.writerow(['Colaborador', 'Salário', 'Departamento', 'Avaliação', 'Admissão'])
        
        # Dados
        for i in range(linhas):
            colaborador = f'Colaborador {i + 1}'
            salario = round(random.uniform(1500, 15000), 2)
            departamento = random.choice(['Vendas', 'T.I.', 'Marketing', 'Financeiro'])
            avaliacao = round(random.uniform(1, 5), 1)
            admissao = (datetime.now() - timedelta(days=random.randint(0, 1825))).strftime('%Y-%m-%d')
            
            escritor.writerow([colaborador, salario, departamento, avaliacao, admissao])

def gerar_dataset_financeiro(linhas):
    """Gera um arquivo CSV financeiro."""
    criar_diretorio_se_nao_existir()

    with open('output/financeiro.csv', 'w', newline='', encoding='utf-8') as arquivo_csv:
        escritor = csv.writer(arquivo_csv)
        
        # Cabeçalho
        escritor.writerow(['Transação', 'Categoria', 'Valor', 'Data'])
        
        # Dados
        for i in range(linhas):
            transacao = f'Transação {i + 1}'
            categoria = random.choice(['Alimentação', 'Transporte', 'Lazer', 'Moradia', 'Salário'])
            
            if categoria == 'Salário':
                valor = round(random.uniform(1500, 15000), 2)
            else:
                # Despesas são negativas
                valor = round(random.uniform(-500, -10), 2)
            
            data = (datetime.now() - timedelta(days=random.randint(0, 365))).strftime('%Y-%m-%d')
            
            escritor.writerow([transacao, categoria, valor, data])

# --- Função Principal ---

def main():
    """Função principal que roda o programa."""
    print("Bem-vindo ao Gerador de CSVs!")
    print("=============================")
    
    while True:
        print("\nQual dataset você quer gerar?")
        print("1 - Vendas")
        print("2 - RH")
        print("3 - Financeiro")
        print("0 - Sair do programa")
        
        opcao = input("Digite a opção: ")
        
        if opcao == '0':
            print("Saindo... Até logo!")
            break
            
        # Pede o número de linhas para o usuário
        try:
            linhas = int(input("Quantas linhas você quer gerar (ex: 100)? "))
        except ValueError:
            print("Isso não é um número. Tente de novo.")
            continue

        

        # Chama a função baseada na escolha do usuário
        if opcao == '1':
            gerar_dataset_vendas(linhas)
            print(f"Arquivo 'vendas.csv' gerado com {linhas} linhas na pasta 'output'.")
        elif opcao == '2':
            gerar_dataset_rh(linhas)
            print(f"Arquivo 'rh.csv' gerado com {linhas} linhas na pasta 'output'.")
        elif opcao == '3':
            gerar_dataset_financeiro(linhas)
            print(f"Arquivo 'financeiro.csv' gerado com {linhas} linhas na pasta 'output'.")
        else:
            print("Opção não reconhecida. Tente de novo.")

# Roda o programa
if __name__ == '__main__':
    main()