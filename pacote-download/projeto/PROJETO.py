from biblioteca import *


if __name__ == '__main__':

    organizar('GESTOR DE VIAGENS MELO')

    while True:

        resposta = menu(['Destinos', 'Alojamentos', 'Consultar dados de um Cliente', 'Agendar Viagem para Cliente', 'Histórico', 'Sair do Programa'])
        if resposta == 1:
            resposta1 = submenu(['Europa', 'América', 'África'])
            if resposta1 == 1:
                print('Os destinos na Europa disponíveis são :')
                Europa = submenu(['França', 'Espanha', 'Holanda', 'Suiça'])
                if Europa == 1:
                    print('Preço França - 200€')
                if Europa == 2:
                    print('Preço Espanha - 125€')
                if Europa == 3:
                    print('Preço Holanda - 170€')
                if Europa == 4:
                    print('Preço Suiça - 150€')
                #no final  é suposto pedir o cliente e nif para adicionar o preço e o destino
                #mudar o menu, separar por funções e recriar o menu (inserir,remover,editar... parte dos destinos)
            elif resposta1 == 2:
                print('Os destinos na América disponíveis são:')
                America = submenu(['Brasil', 'Chile', 'Argentina'])

            elif resposta1 == 3:
                print('Os destinos na Africa disponiveis são:')
                Africa = submenu(['Angola', 'Guiné', 'Moçambique'])

        elif resposta == 2:
            organizar('ALOJAMENTOS')
            lista = submenu(['Inserir', 'Editar','Remover', 'Lista'])
            if lista == 1:
                nome = str(input('Nome do alojamento :'))
                descricao = str(input('Descrição do alojamento:'))
                morada = str(input('Morada do alojamento:'))
                preco = float(input('Preço:(€)'))

                #Isto tem que ser adicionado ao ficheiro txt.
            if lista == 2:
                organizar('EDITAR')
                #print da lista de alojamentos e escolher por opção qual editar
            if lista == 3:
                organizar('REMOVER')
                #print da lista de alojamentos e escolher por opção qual remover da lista
            if lista == 4:
                print(alojamentos)

        elif resposta == 3:
            organizar('CLIENTES')
            lista = submenu(['Inserir', 'Editar', 'Remover', 'Lista de Clientes'])
            if lista == 1:
                nome = str(input('Nome do cliente :'))
                nif = str(input('Nif do cliente:'))
                with open("clientes.txt", "a") as addclientes:
                    addclientes.write(str('Nome: ') + (nome) )
                    addclientes.write(str(' ') + ('NIF: ') + (nif) + '\n')


            if lista == 2:
                nome = str(input('Nome do cliente :'))
                nif = int(input('Nif do cliente:'))
            if lista == 3:
                print('cliente')
                #Primeira parte ler a lista de clientes

                #Pedir um input com o NIF que pretendo remover

                #Verificar se o NIF existe na lista

                    #Se sim substituir esse NIF por uma linha em branco na variável e reescrever para o ficheiro txt.

                    #Caso não exista, verificar novamente ou sair do programa

                

            if lista == 4:
                print(clientes)

        elif resposta == 4:
            organizar('AGENDAR VIAGEM')
            lista = submenu(['Destino', 'Alojamento', 'Destino e Alojamento'])
            if lista == 1:
                print('Lista dos destinos')
                #escolher qual o cliente deseja.
                #guardar com o seu nome de nif
            if lista == 2:
                print(destinos)
                # escolher qual o cliente deseja.
                # guardar com o seu nome de nif
            if lista == 3:
                print(destinos, alojamentos)
                # escolher qual o cliente deseja.
                # guardar com o seu nome de nif
        elif resposta == 5:
            organizar('HISTÓRICO')
            #através do nome e nif do cliente é suposto conseguir aceder a todas viagens já agendadas ,
            #tanto para o futuro como as atuais/passadas.

        elif resposta == 6:
            print('A desligar o sistema... Obrigado')
            break
        else:
            print('Erro! Digite uma opção válida')
