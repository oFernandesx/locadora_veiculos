import os
from classes import *
from defs import *
from aslistas import *

while True:
    while True:
        try:
            escolha = menu()
            os.system('cls')
            break

        except Exception as e:
            print(f'Opção inválida, o erro foi {e}')
            limpeza()
    
    match escolha:
        case 1: #Cadastrar veículo
            while True:
                escolha_cadastrar = cadastrar()
                os.system('cls')
                match escolha_cadastrar:
                    case 1:
                        veiculos.append(cad_carro())
                        break
                    case 2:
                        veiculos.append(cad_moto())
                        break
                    case 0:
                        break
                    case _:
                        print("Opção inválida")
                        limpeza()


        case 2: #Alugar veículo
            escolha_alugar = alugar()
            match escolha_alugar:
                case 1:
                    pass
                

        case 3: #Veículos cadastrados/alugados
            acao_veiculo()
            
        
        case 4: #Sair
            os._exit(3)
            os.system("cls")

        case _: #Erro
            print('Opção inválida!')
            limpeza()
            os.system("cls")