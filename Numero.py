import random
import json
import datetime

secret = random.randint(1, 10)
attempts = 0
tent_erradas = []

jogo = True

with open("score_list.json", "r") as score_file:
    score_list = json.loads(score_file.read())

def jogar():
    while jogo:
        guess = int(input("Adivinha o número secreto de 1 a 10"))
        attempts += 1

        if guess == secret:
        print("Parabéns, adivinhaste! O núemero era o " + str(secret))
        print("Foi à " + str(attempts) + "ª tentativa")

        score_data = {"Tentativas": attempts, "data": str(datetime.datetime.now()), "jogador": nome, "segredo": secret, "tentativas": tent_erradas}


print("Bem vindo ao número virtual")
escolha

