import sys
import sqlite3
import time
import os

conectar = sqlite3.connect('academia.db')
c = conectar.cursor()


def login(query):
    c.execute("CREATE TABLE IF NOT EXISTS login (id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT NOT NULL UNIQUE,email TEXT NOT NULL UNIQUE,password TEXT NOT NULL)")
    conectar.commit()


def inserir(nomeCliente, telefone, email, cdCidade, cdModalidade, cdTurno, cdInstrutor):
    c.execute('INSERT INTO cliente VALUES(?, ?, ?, ?, ?, ?, ?)', (nomeCliente,
              telefone, email,  cdCidade, cdModalidade, cdTurno, cdInstrutor))
    conectar.commit()


def listar(p):
    sql = 'SELECT nomeCliente, telefone, email FROM cliente WHERE nomeCliente = ?'
    for row in c.execute(sql, (p,)):
        print('DADOS: ', row)


fc = int(
    input('\n\n################ BEM VINDO AO SISTEMA DA ACADEMIA POTENAY ################\n\n[1] Cadastrar\n[2] Ver perfil\n[3] Log-in\n[0] Sair\n\nO que voce deseja fazer?: '))

if fc == 1:
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n\n################ CADASTRO ACADEMIA POTENAY ################\n")
        nomeCliente = str(input('Digite um nome: '))
        telefone = str(input('Digite um telefone: '))
        email = str(input('Digite um e-mail: '))
        os.system('cls' if os.name == 'nt' else 'clear')
        cdCidade = int(input(
            'Digite a cidade:\n1 - Cachoeiro de Itapemirim\n2 - Vitória\n3 - Vila Velha\n4 - Domingos Martins\n5 - Vargem Alta\n6 - Venda Nova\n\nDigite uma Opcao: '))
        os.system('cls' if os.name == 'nt' else 'clear')
        cdModalidade = int(input(
            'Digite uma:\n1 - Natação\n2 - Musculação\n3 - Funcional\n4 - Crossfit\n5 - Box\n\nDigite uma Opcao: '))
        os.system('cls' if os.name == 'nt' else 'clear')
        cdTurno = int(
            input('Digite o turno:\n1 - Manhã\n2 - Tarde\n3 - Noite\n\nDigite uma Opcao: '))
        os.system('cls' if os.name == 'nt' else 'clear')
        cdInstrutor = int(input(
            'Digite o instrutor:\n1234 - Francisco Junior\n2145 - Igor Manoel\n3045 - Jeane da Silva\n4451 - Marcos de Sá\n\nDigite uma Opcao: '))

        inserir(nomeCliente, telefone, email, cdCidade,
                cdModalidade, cdTurno, cdInstrutor)
    except:
        print('\nErro ao cadastrar, tente novamente mais tarde!')
    else:
        print('\nCadastro com sucesso')

if fc == 2:
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n\n################ VER PERFIL ACADEMIA POTENAY ################\n")
        p = str(input('Digite um nome: '))
        listar(p)
    except:
        print('\nErro ao pesquisar, tente novamente mais tarde!')
    else:
        print('...')

if fc == 3:
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n\n################ LONG-IN ACADEMIA POTENAY ################\n")

        query = input(
            'Bem vindo\nEntre com "Login" se já tem uma conta ou se não entre com "Registrar": ')
        login(query)
        if query == "Registrar":
            while True:
                name = input("\nEntre com seu nome: ")
                n = c.execute('SELECT name FROM login').fetchone()
                n = str(n).strip("('',)'")
                if n == name:
                    print('\nEsse nome de usuário já existe, tente outro!')
                    continue
                else:
                    while True:
                        email = input("\nEntre com seu email: ")
                        m = c.execute('SELECT email FROM login').fetchone()
                        m = str(m).strip("('',)'")
                        if m == email:
                            print(
                                'Já está em nosso banco de dados, digite outro!')
                            continue
                        else:
                            while True:
                                password = input("Entre com sua senha: ")
                                rpassword = input(
                                    "Entre com sua senha novamente! ")
                                if password == rpassword:
                                    c.execute('INSERT INTO login VALUES(?,?,?,?)',
                                              (None, name, email, password))
                                    conectar.commit()
                                    print('Você está logado agora!')
                                    sys.exit()

                                else:
                                    print('Senha não corresponde!')
                                    continue

        elif query == "Login":
            while True:
                name = input("Entre com seu nome: ")
                password = input("Entre com sua senha: ")
                n = c.execute(
                    "SELECT name from login WHERE name='"+name+"'").fetchone()
                n = str(n).strip("('',)'")
                if n == name:
                    pw = c.execute(
                        "SELECT password from login WHERE password='" + password + "'").fetchone()
                    pw = str(pw).strip("('',)'")
                    if pw == password:
                        print('Você está logado agora!\n')
                        break
                    else:
                        print('Senha errada.')
                else:
                    print('Nome errado.')
        else:
            print('Entrada incorreta. Tente novamente. ')
    except:
        fc
    else:
        print('...')
    conectar.close()


if fc == 0:
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('\nSaindo... Aguarde...\n')
        time.sleep(1)
        print("\nObrigado por utilizar nosso sistema! Volte sempre!!!\n")
    except:
        exit()
    else:
        print('...')
