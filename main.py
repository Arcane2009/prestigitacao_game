print("-------------------------------")
print("\nBem vindo ao jogo da prestigitação!\n")
print("-------------------------------")

n_secreto = 3308

entrada = int(input("Digite um número: "))
acertou = entrada == n_secreto
entrada_maior = entrada > n_secreto
entrada_menor = entrada < n_secreto

print(f"\nVocê digitou o número: {entrada}")

if(acertou):
    print("Parabéns, você acertou o número secreto")
else:
    if(entrada_maior):
        print("Você errou! O número digitado foi maior que o secreto")
    if(entrada_menor):
        print("Você errou! O número digitado foi menor que o secreto")

print("\nFim de jogo")