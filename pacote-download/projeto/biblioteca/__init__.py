def ler(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('ERRO:por favor, digite um número inteiro válido.')
            continue
        except (KeyboardInterrupt):
            print('Usuário preferiu não digitar esse número.')
            return 0
        else:
            return n



def linha(tam = 43):
    return '_' * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabecalho('Menu Principal')
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c = c + 1
    print(linha())
    opc = ler('Sua Opção: ')
    return opc

def submenu(lista):
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c = c + 1
    print(linha())
    opc = ler('Sua Opção: ')
    return opc

def organizar(titulo):
    print('=-' * 25)
    print(titulo.center(45))
    print('=-' * 25)

with open("clientes.txt", "r") as clientes:
    clientes = clientes.read()

with open("alojamentos.txt", "r") as alojamentos:
    alojamentos = alojamentos.read()

with open("destinos.txt", "r") as destinos:
    destinos = destinos.read()
