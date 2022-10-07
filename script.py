print("OLá, seja bem vindo(a)!")
print("Iremos analisar o seu imc agora, por favor digite as seguintes informações: ")
peso = float(input("Qual o seu peso??"))
altura = float(input("Qual a sua altura??"))
imc = peso / (altura * altura)
if imc < 18.5:
    print("abaixo do peso")
elif 18.5 <= imc <= 24.99:
    print("peso Normal")
elif 25 <= imc <= 29.99:
    print("acima do peso")
else:
    print("Obeso(a)")
