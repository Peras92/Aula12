import random
import json
import datetime



with open("score_list.json", "r") as score_file:
    score_list = json.loads(score_file.read())

def jogar():
    secret = random.randint(1, 10)
    attempts = 0
    tent_erradas = []

    jogo = True

    while jogo:

        

        guess = int(input("Adivinha o número secreto de 1 a 10: "))
        attempts += 1

        if guess == secret:
            print("Parabéns, adivinhaste! O número era o " + str(secret))
            print("Conseguiste à " + str(attempts) + "ª tentativa")
            nome = input("Por favor indica o teu nome: ")

            score_data = {"Tentativas": attempts, "data": str(datetime.datetime.now()), "jogador": nome, "segredo": secret, "tentativas": tent_erradas}

            score_list.append(score_data)

            with open("score_list.json", "w") as score_file:
                score_file.write(json.dumps(score_list))

            jogo = False
            
        elif guess > secret:
            tent_erradas.append(guess)
            print("Tenta um número mais pequeno")
        elif guess < secret:
            tent_erradas.append(guess)
            print("Tenta um número maior")



print("Bem vindo ao número virtual")

jogar()

