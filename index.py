from random import randint
from time import sleep

def ataque_usuario():
    print('\036'*30)
    print(' == Escolha seu ataque == ')
    print('\036'*30)
    print('(1) \032 Soco')
    print('(2) \032 Especial')
    return int(input())



def ataque_computador():
    rand = randint(1, 3)
    return rand

def print_hp(HPusuario, HPcomputador, contEspeciais):
    print('\04'*30)
    print('HP \032 usuario: ',HPusuario)
    print('HP \032 computador: ',HPcomputador)
    print('Contagem de especiais: ',contEspeciais)

def batalha():
    HPusuario = 150
    HPcomputador = 0
    contEspeciais = 5
    escolhaAtaque = 0
    i = 1

    while(HPusuario > 0):
        HPcomputador = 10 + i

        print('\05'*30)
        print(' \020 INIMIGO: ',i)
        print('\05'*30+'\n')

        while(HPcomputador > 0 and HPusuario > 0):
            print_hp(HPusuario, HPcomputador, contEspeciais)
            escolhaAtaque = ataque_usuario()


            if(escolhaAtaque == 1):
                print('>>> Usuario deu um soco! \n')
                HPcomputador -= 7
            elif(escolhaAtaque == 2 and contEspeciais > 0):
                print('>>> usuario deu um especial! \n')
                HPcomputador -= 20
                contEspeciais -= 1
            else:
                print('>>> opção invalida \n')
            sleep(2)


            if(HPcomputador > 0):
                escolhaAtaque = ataque_computador()

                if(escolhaAtaque == 1):
                    print('>>> computador deu um soco! \n'+'\07'*3)
                    sleep(2)
                    HPusuario -= 3 + int(i / 10)
                elif(escolhaAtaque == 2):
                    print('>>> computador deu um chute! \n'+'\07'*3)
                    sleep(2)
                    HPusuario -= 5 + int(i / 10)
                elif(escolhaAtaque == 3):
                    print('>>> computador deu um especial!! \n'+'\07'*3)
                    sleep(2)
                    HPusuario -= 8 + int(i / 20)
            else:
                print('\06 INIMIGO DERROTADO!! \06 \n'+'\07'*8)
                sleep(3)
                i+=1

        if(HPusuario > 0):
            HPusuario += 5
            if(HPusuario > 150):
                HPusuario = 150

            if(i % 10 == 0):
                contEspeciais += 1
                if(contEspeciais > 5):
                    contEspeciais = 5
    
        
continua = 's'
while(continua == 's'):
    batalha()

    print('Fim de jogo. dejesa continuar? (s/n)')
    continua = input()