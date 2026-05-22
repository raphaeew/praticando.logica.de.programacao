import csv
import os

def salvaremexcel(contatos):
    with open('contatos.csv', mode='w', newline='', encoding='utf-8') as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(['Nome', 'Contato', 'Email'])
        for contato in contatos:
            escritor.writerow([contato['Nome'], contato['Contato'], contato['Email']])

def carregardados():
    contatos = []
    nome_arquivo = 'contatos.csv'
    if os.path.exists(nome_arquivo):
        with open(nome_arquivo, mode='r', encoding='utf-8') as arquivo:
            leitor = csv.DictReader(arquivo)
            for linha in leitor:
                contatos.append(linha)
    return contatos

def adicionarcontato(contatos):
    Nome = input('Digite o nome do contato:') 
    Contato = input('Digite o número de contato:')
    Email = input('Digite o email do contato:')
    contatos.append({'Nome': Nome, 'Contato': Contato, 'Email': Email})
    print('Contato adicionado com sucesso!')
    salvaremexcel(contatos)

def listarcontatos(contatos):
    print('Lista de contatos:')

    if not contatos:
        print('Nenhum contato encontrado.')
    for contato in contatos:
        print(f'Nome: {contato["Nome"]}, Contato: {contato["Contato"]}, Email: {contato["Email"]}')
    salvaremexcel(contatos)
    
def editarcontato(contatos):
    Nome = input('Qual contato deseja editar?')
    if Nome in contatos:
        print('Esse contato não existe!')
    
    if Nome in contatos:
        Contato = input('Digite o novo número de contato: ')
        Email = input('Digite o novo email: ')
        contatos[Nome]['Contato'] = Contato
        contatos[Nome]['Email'] = Email
        print('Contato editado com sucesso!')
    salvaremexcel(contatos)

def excluircontato(contatos):
    Nome = input('Qual contato deseja excluir?')
    if Nome in contatos:
        del contatos[Nome]
        print('Contato excluído com sucesso!')
    else:
        print('Esse contato não existe!')
    salvaremexcel(contatos)


def menu():
    contatos = carregardados()
    while True:
        print('\n MENU DE CONTATOS')
        print('1. Adicionar contato')
        print('2. Listar contatos')
        print('3. Editar contato')
        print('4. Gerar Excel')
        print('5. Excluir contato')
        print('6. Sair')

        opcao = input('Escolha uma opção: ')

        if opcao == '1':
            adicionarcontato(contatos)
        elif opcao == '2':
            listarcontatos(contatos)
        elif opcao == '3':
            editarcontato(contatos)
        elif opcao == '4':
            salvaremexcel(contatos)
        elif opcao == '5':
            excluircontato(contatos)
        elif opcao == '6':
            salvaremexcel(contatos)
            print('Saindo...')
            break
        else:
            print('Opção inválida!')

menu()