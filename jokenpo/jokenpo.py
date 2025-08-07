from random import randint
from time import sleep

cont = 0

while True:
    eu = input('Escolha uma sua opção [Pedra/Papel/Tesoura]: ').lower().strip()
    if eu not in ['pedra', 'papel', 'tesoura']:
        print('Opção inválida. Tente novamente.')
        continue
    computador = randint(1,3)

    if computador == 1:
        computador = 'pedra'
    elif computador == 2:
        computador = 'papel'
    else:
        computador = 'tesoura'
    
    print('Vamos começar')
    sleep(0.5)
    print('jo')
    sleep(1)
    print('ken')
    sleep(1)
    print('po')
    sleep(0.5)

    # tesoura e papel
    if computador == 'papel' and eu == 'tesoura':
        print(f'Voce colocou {eu} e eu colocoquei {computador}')
        print(f'Dessa voce ganhoi ')
        cont +=1
        verificador = input('quer continuar? [s/n]').lower().strip()
        if verificador == 'n':
            break

    elif computador == 'tesoura' and eu == 'papel' or computador == 'pedra' and eu == 'tesoura':
        print(f'Voce colocou {eu} e eu colocoquei {computador}')
        print(f'Dessa eu ganhei')
        verificador = input('quer continuar? [s/n]').lower().strip()
        if verificador == 'n':
            break

    # pedra e papel
    elif computador == 'pedra' and eu == 'papel' or computador == 'tesoura' and eu == 'pedra':
        print(f'Voce colocou {eu} e eu colocoquei {computador}')
        print(f'Dessa você ganhou ')
        cont += 1
        verificador = input('quer continuar? [s/n]').lower().strip()
        if verificador == 'n':
            break

    elif computador == 'papel' and eu == 'pedra':
        print(f'Voce colocou {eu} e eu colocoquei {computador}')
        print(f'Dessa vez eu ganhei')
        verificador = input('quer continuar? [s/n]').lower().strip()
        if verificador == 'n':
            break

    elif computador == 'pedra' and eu == 'pedra' or computador == 'papel' and eu == 'papel' or computador == 'tesoura' and eu == 'tesoura':
        print(f'voce colocou {eu} e eu ocloquei {computador} entao empatamos')
        verificador = input('quer continuar? [s/n]').lower().strip()
        if verificador == 'n':
            break

if cont != 0:
    print(f'Agradeço pelo jogo voce ganhou {cont} vezes de mim parabens')
    print('volte sempre')
else:
    print(f'Agradeço pelos jogos')
    print('volte sempre')