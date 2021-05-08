import random
import json
import datetime

#Abre a lista de resultados que é usada mais tarde
with open("score_list.json", "r") as score_file:
    score_list = json.loads(score_file.read())

#Função que define o jogo
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

            score_data = {"Tentativas": attempts, "data": str(datetime.datetime.now()), "jogador": nome, "segredo": secret, "errados": tent_erradas}

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

#Função que dá o high score
def ranking():
    high_score=sorted(score_list, key=lambda i: i["Tentativas"])

    print("High Scores - Top 10")

    for score_dict in high_score[:10]:
        print("O Jogador {0} conseguiu acertar em {1} tentativas. O número era o {3} e os números que ele errou foram os seguintes {4}".format(score_dict.get("jogador"), str(score_dict.get("tentativas")), score_dict.get("data"), score_dict.get("segredo"), score_dict.get("errados")))


menu = True #serve para parar o ciclo do jogo

print("Bem vindo ao número virtual") 
while menu:
    escolha = input("Pretendes jogar (A), ver os nossos 10 melhores jogadores (B) ou sair (C)? ")

    if escolha.upper() == "A":
        jogar()

    elif escolha.upper() == "B":
        ranking()

    elif escolha.upper() != "C":
        escolha = input("Escolhe uma opção permitida: ")

    else :
        menu = False
