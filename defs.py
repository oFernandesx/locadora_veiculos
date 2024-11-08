import os
from classes import *
from aslistas import *

def limpeza():
    os.system("pause")
    os.system("cls")
    return limpeza

def menu():
    while True:
        try:
            print("--- LOCADORA DE VEÍCULOS ---")
            print("\nBem-vindo, o que você deseja fazer?")
            escolha = int(input("1 - Cadastrar veículo\n2 - Alugar veículo\n3 - Exibir Veículos\n4 - Sair\n-->  "))
            return escolha
        except Exception as e:
            print(f'Opção inválida, o erro foi {e}')
            os.system('cls')



def cadastrar():
    while True:
        try:
            print("--- CADASTRAR VEÍCULO ---")
            print("\nQual veículo deseja cadastrar?")
            escolha = int(input("0 - Sair\n1 - Carro\n2 - Moto\n--> "))
            return escolha
        except Exception as e:
            print(f'Opção inválida, o erro foi {e}')
            os.system('cls')


def alugar():
    while True:
        print("--- ALUGAR VEÍCULO ---")
        if len(veiculos) <= 0:
            print('Não existe nenhum Carro cadastrado')
            os.system('pause')
            os.system('cls')
            return
        else:
            cont = 1
            print('ID\ttipo\tmodelo\t\tmarca\t\tstatus') 
            for e in veiculos:
                print(f'{cont}º \t{e.getTipo()}\t{e.getModelo()}\t{e.getMarca()}\t\t{e.getStatus()}') 
                cont += 1
            print('digite \"0\" para sair')
            try:
                choise = int(input('Informe o ID do Veiculo que deseja alugar\n-->'))
                os.system('cls')
                try:
                    if choise != 0:
                        if veiculos[choise - 1].getStatus() == "Disponivel":
                            veiculos[choise - 1].setStatus("Alugado")
                            print('Carro Alugado com sucesso ')
                        elif veiculos[choise - 1].getStatus() == "Alugado":
                            print('Este veiculo Não esta disponivel')
                            limpeza()
                        else:
                            break

                except Exception as e:
                    print(f'Opção inválida, o erro foi {e}')
                    limpeza()


                os.system('pause')
                os.system('cls')
                #CONTINUAR CODIGO
                return choise

            except Exception as e:
                    print(f'Opção inválida, o erro foi {e}')
                    limpeza()

def acao_veiculo():
    while True:
        print('Qual opcao deseja - - ')
        print('1 - Exibir veiculos')
        print('2 - Utilizar veiculo')
        print('3 - Sair')
        try:
            escolha = int(input('--> '))
            os.system('cls')
            match escolha:
                case 1:
                    print('Veiculos - -') 
                    cont = 1 
                    print('ID\ttipo\tmodelo\t\tmarca\t\tstatus') 
                    for carritos in veiculos: 
                        print(f'{cont}º \t{carritos.getTipo()}\t{carritos.getModelo()}\t{carritos.getMarca()}\t\t{carritos.getStatus()}') 
                        cont += 1
                    limpeza()
                case 2:
                    cont = 1 
                    print('ID\ttipo\tmodelo\t\tmarca\t\tstatus') 
                    for carritos in veiculos: 
                        print(f'{cont}º \t{carritos.getTipo()}\t{carritos.getModelo()}\t{carritos.getMarca()}\t\t{carritos.getStatus()}') 
                        cont += 1
                    print('digite \"0\" para sair')
                    escolha = int(input('informe o ID do veiculo que deseja Utilizar\n--> '))
                    os.system('cls')
                    if escolha != 0:
                        if veiculos[escolha - 1].getStatus() == "Disponivel":
                            print('Este veículo não esta alugado\nVocê deve alugar o veiculo para utiliza-lo')
                            limpeza()
                        elif veiculos[escolha - 1].getStatus() == "Alugado":
                            if veiculos[escolha - 1].getTipo() == "Moto":
                                while True:
                                    print('Você subiu na moto')
                                    escolha = int(input('1 - Dar grau\n2 - Sair da Moto\n--> '))
                                    os.system('cls')
                                    try:
                                        match escolha:
                                            case 1:
                                                veiculos[escolha - 1].dar_grau()
                                                limpeza()
                                            case 2:
                                                break
                                            case _:
                                                print("Opção invalida")
                                                limpeza()
                                    except Exception as e:
                                        print(f'Opção inválida, o erro foi {e}')
                                        limpeza()
                            
                            elif veiculos[escolha - 1].getTipo() == "Carro":
                                    while True:
                                        print('Você entrou no carro')
                                        escolha = int(input('1 - Cantar Pneu\n2 - Sair do carro\n--> '))
                                        os.system('cls')
                                        try:
                                            match escolha:
                                                case 1:
                                                    veiculos[escolha - 1].cantar_pneu()
                                                    limpeza()
                                                case 2:
                                                    break
                                                case _:
                                                    print("Opção invalida")
                                                    limpeza()
                                        except Exception as e:
                                            print(f'Opção inválida, o erro foi {e}')
                                            limpeza()
                                    
                
                case 3:
                    break

                case _:
                    print("Opção invalida")
                    limpeza()

            return escolha

        except Exception as e:
            print(f'Opção inválida, o erro foi {e}')
            limpeza()





def cad_carro():
    print("--- CADASTRAR CARRO ----")
    print("")
    while True:
        try:
            marca = input("\nInsira a marca do carro: ")
            modelo = input("Insira o modelo do carro: ")
            ano = int(input("Insira o ano do carro: "))
            carro = Carro(marca, modelo, ano)
            carro.setStatus("Disponivel")
            carro.setTipo("Carro")
            print("\nCarro cadastrado com sucesso!\n")
            limpeza()
            return carro
        except Exception as e:
            print(f'Opção inválida, o erro foi {e}')
            limpeza()
        
    

def cad_moto():
    print("--- CADASTRAR MOTO ----")
    print("")
    while True:
        try:

            marca = input("\nInsira a marca da moto: ")
            modelo = input("Insira o modelo da moto: ")
            ano = input("Insira o ano da moto: ")
            moto = Moto(marca,modelo,ano)
            moto.setStatus("Disponivel")
            moto.setTipo("Moto")
            print("\nMoto cadastrado com sucesso!\n")
            limpeza()
            return moto
        except Exception as e:
            print(f'Opção inválida, o erro foi {e}')
            limpeza()
        
