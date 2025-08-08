import random

# Lendo as palavras do arquivo
with open("palavras.txt", "r", encoding="utf-8") as f:
    palavras = [linha.strip() for linha in f]

def desenhar_forca(erros):
    if erros == 1:
        print("     _____")
        print("    /     \\")
        print("   |        |")
        print("    \\     /")
        print("     |||||")
    if erros == 2:
        print("     _____")
        print("    /     \\")
        print("   | () () |")
        print("    \\  ^  /")
        print("     |||||")
    elif erros == 3:
        print("     _____")
        print("    /     \\")
        print("   | () () |")
        print("    \\  ^  /")
        print("     |||||")
        print("   __|||||")
        print("  /  |||||")
        print(" |   |||||")
    elif erros == 4:
        print("     _____")
        print("    /     \\")
        print("   | () () |")
        print("    \\  ^  /")
        print("     |||||")
        print("   __|||||__")
        print("  /  |||||  \\")
        print(" |   |||||   |")
    elif erros == 5:
        print("     _____")
        print("    /     \\")
        print("   | () () |")
        print("    \\  ^  /")
        print("     |||||")
        print("   __|||||__")
        print("  /  |||||  \\")
        print(" |   |||||   |")
        print("     || ||")
        print("     ||")
        print("    [] ")
    elif erros == 6:
        print("     _____")
        print("    /     \\")
        print("   | () () |")
        print("    \\  ^  /")
        print("     |||||")
        print("   __|||||__")
        print("  /  |||||  \\")
        print(" |   |||||   |")
        print("     || ||")
        print("     || ||")
        print("    []   []")

def palavra_esta_nas_listas(palavra, listas):
    for categoria, palavras in listas.items():
        if palavra in palavras:
            return True, categoria  # Retorna True e o nome da categoria
    return False, None  # Não encontrada


listas = {
    "casa_e_objetos": [
        "casa", "porta", "mesa", "cadeira", "janela",
        "roupa", "sapato", "camisa", "calça", "brinquedo",
        "flor", "árvore"
    ],
    "transporte_e_locais": [
        "carro", "rua", "praça", "escola"
    ],
    "natureza_e_clima": [
        "sol", "chuva", "vento", "terra", "céu", "estrela"
    ],
    "tempo": [
        "tempo", "dia", "noite", "hoje", "ontem", "amanhã",
        "sempre", "nunca", "agora", "depois", "antes"
    ],
    "pessoas_e_relacoes": [
        "gente", "amigo", "mãe", "pai", "filho", "filha"
    ],
    "comida_e_bebida": [
        "comida", "água", "leite", "pão", "fruta",
        "arroz", "feijão", "carne", "peixe"
    ],
    "trabalho_e_dinheiro": [
        "trabalho", "dinheiro", "comprar", "vender",
        "gastar", "ganhar"
    ],
    "estudo_e_comunicacao": [
        "escola", "livro", "caneta", "papel",
        "telefone", "celular", "computador", "internet"
    ],
    "arte_e_entretenimento": [
        "foto", "vídeo", "música", "filme", "jogo", "bola"
    ],
}





while True:
    palavra_aleatoria = random.choice(palavras).lower()
    tamanhoPalavra = len(palavra_aleatoria)
    palavra = "_" * tamanhoPalavra
    erros = 0
    letraErradas = []

    encontrada, categoria = palavra_esta_nas_listas(palavra_aleatoria, listas)

    

    print("\nVamos começar nosso jogo de forca!!")

    if encontrada:
        print(f"🔍 Dica: A palavra está na categoria: {categoria.replace('_', ' ')}")

    print(f"A palavra sorteada tem {tamanhoPalavra} letras")

    print(palavra)

    
    while True:
        letra = input("\nEscolha uma letra: ").lower()
        
        if len(letra) != 1 or letra.isnumeric():
            print('Quantia de letra ou dado invalido')
            continue

        if letra in palavra_aleatoria:
            quantia = palavra_aleatoria.count(letra)
            print(f"A letra '{letra}' aparece {quantia}x na palavra.")

            lista = list(palavra)
            for i, l in enumerate(palavra_aleatoria):
                if l == letra:
                    lista[i] = letra
            palavra = "".join(lista)

            print(palavra)

            if "_" not in palavra:
                print("🎉 Parabéns! Você acertou a palavra!")
                break
        else:
            letraErradas.append(letra)
            erros += 1
            print(f"A letra '{letra}' não está na palavra.")
            print(f"Letras erradas: {', '.join(letraErradas)}")
            desenhar_forca(erros)

            if erros == 6:
                print(f"💀 Você perdeu! A palavra era: {palavra_aleatoria}")
                break

    continuar = input("Quer jogar novamente? (s/n): ").lower()
    if continuar != "s":
        print("Até a próxima!")
        break
