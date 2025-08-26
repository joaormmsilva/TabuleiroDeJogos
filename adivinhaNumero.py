import random
from time import sleep

partidas = 0
acerto = 0
erro = 0
print(f'Olá vamos jogar um jogo de adivinhação, vou gerar um numero aleatorio de 1 a 10 e voce tera que adivinhar ele')

while True:
    numeroAleatorio = random.randint(1,10)
    resposta = int(input('Escolha qual o numero você acha que eu coloquei: '))
    if resposta > 10:
        
        print('❌ Esse numero esta fora dos numeros que podem ser sorteados escolha outro entre 1 e 10')
        continue

    if resposta == numeroAleatorio:
        print('e a reposta esta...')
        sleep(1)
        print(f'✅ Certa, parabens voce acertou eu escolhi o numero {numeroAleatorio}')
        acerto += 1
        partidas += 1
        verificador = input(f'Quer continuar o jogo atualmente voce esta com {acerto} acerto e {erro} erros [s/n]: ').lower().strip()
        if verificador in ['sim','s','continuar']:
            continue
        if verificador in ['nao','não','n','sair']:
            break
        if verificador not in ['nao','não','n','sair']:
            verificador2 = input('Resposta fora dos padrões quer sair? [s/n]')
        if verificador2 == 's':
            break 
    else:
        print('e a reposta esta...')
        sleep(1)
        print(f'❌ errada eu escolhi o numero {numeroAleatorio}')
        erro += 1
        partidas += 1
        verificador = input(f'Quer continuar o jogo atualmente voce esta com {acerto} acerto e {erro} erros [s/n]: ').lower().strip()
        if verificador in ['sim','s','continuar']:
            continue
        if verificador in ['nao','não','n','sair']:
            break
        if verificador not in ['nao','não','n','sair']:
            verificador2 = input('Resposta fora dos padrões quer sair? [s/n]')
        if verificador2 == 's':
            break 
        
print(f'Obrigado por jogar comigo o resultado final das {partidas} partidas foi {acerto} acertos e {erro} erros')
