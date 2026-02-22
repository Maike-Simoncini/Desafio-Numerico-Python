import random
import time

def line():
    print("-" * 36)

def jogar():
    attempts = 1
    guesses = []
    
    levels = {
        1: {'Level': 'Fácil', 'Chances': 10},
        2: {'Level': 'Médio', 'Chances': 5},
        3: {'Level': 'Difícil', 'Chances': 3}
    }

    line()
    print("Bem-vindo ao Jogo de Adivinhação!")
    line()
    print("Selecione o nível de dificuldade:")

    for key, info in levels.items():
        print(f"{key}. {info['Level']} ({info['Chances']} chances)")

    line()

    # Validação simples para escolha do nível
    try:
        choice = int(input("Digite sua escolha de nível (1, 2 ou 3): "))
        if choice not in levels:
            raise ValueError
    except ValueError:
        print("Opção inválida! Iniciando no nível Fácil por padrão.")
        choice = 1

    level = levels[choice]['Level']
    chances = levels[choice]['Chances']
    computer_random = random.randint(1, 100)

    print(f"\nÓtimo! Dificuldade {level} selecionada.")
    print(f"Você tem {chances} chances para acertar.")
    time.sleep(1)
    print("\nEstou pensando em um número entre 1 e 100...")
    time.sleep(1.5)
    print("Vamos começar!")

    while attempts <= chances:
        try:
            guess = int(input(f"\nTentativa {attempts}/{chances} - Digite seu palpite: "))
        except ValueError:
            print("Por favor, digite apenas números inteiros!")
            continue

        if guess == computer_random:
            print(f"\n✨ PARABÉNS! Você acertou o número '{computer_random}' em {attempts} tentativas.")
            return # Sai da função de jogo após vencer

        else:
            dica = "menor" if guess > computer_random else "maior"
            print(f"Incorreto! O número é {dica} do que {guess}.")
            guesses.append(guess)
            attempts += 1

    # Se sair do loop while, é porque as chances acabaram
    print(f"\n❌ Suas chances acabaram! ({attempts - 1}/{chances})")
    print(f"Seus palpites foram: {', '.join(map(str, guesses))}")
    print(f"O número correto era: {computer_random}")

# --- Loop Principal para Reiniciar ---
while True:
    jogar()
    line()
    dnv = input("Deseja jogar novamente? (S/N): ").strip().upper()
    if dnv != 'S':
        print("\nObrigado por jogar! Até a próxima.")
        break
