from collections import Counter
import os

texto = input('digite sua mensagem: ')

menu = 0
while menu != 7:
    try:
        menu = int(input('escolha uma das opcoes: \n1 - Colocar texto em maiusculo \n2 - Colocar texto em minusculo \n3 - Separar texto \n4 - Contar palavras \n5 - Contar caracteres \n6 - Soma caracteres \n7 - Sair \nopção: '))
            
        if menu == 1:
            os.system('cls')
            print('opcao 1 escolhida: ')
            maicusculo = texto.upper()
            print(maicusculo)
            print('----------------------------------------')
            os.system('pause')
        elif menu == 2:
            os.system('cls')
            print('opcao 2 escolhida: ')
            minusculo = texto.lower()
            print(minusculo)
            print('----------------------------------------')
            os.system('pause')
        elif menu == 3:
            os.system('cls')
            print('opcao 3 escolhida: ')
            separar = texto.split()
            print(separar)
            print('----------------------------------------')
            os.system('pause')
        elif menu == 4:
            os.system('cls')
            print('opcao 4 escolhida: ')
            aparicoes = Counter()
            for palavra in texto.split():
                aparicoes[palavra] += 1
            print(aparicoes)
            print('----------------------------------------')
            os.system('pause')
        elif menu == 5:
            os.system('cls')
            print('opcao 5 escolhida: ')
            aparicoes = Counter(texto)
            print(aparicoes)
            print('----------------------------------------')
            os.system('pause')
        elif menu == 6:
            os.system('cls')
            print('opcao 6 escolhida: ')
            aparicoes = Counter(texto)
            soma = sum(aparicoes.values())
            print('soma: ',soma, 'caracteres')
            print('----------------------------------------')
            os.system('pause')
        elif menu == 7:
            print('opcao 7 escolhida: ')
            print('Fechando programa!')
            print('----------------------------------------')
        else:
            os.system('cls')
            print( 'Opcao invalida!')
            os.system('pause')
    except:
        os.system('cls')
        print('Opcao invalida!')
        os.system('pause')


        
        

        
        







