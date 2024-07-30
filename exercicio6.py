""" Faça um programa que permita ao usuário digitar o seu nome e
em seguida mostre o nome do usuário de trás para frente
utilizando somente letras maiúsculas. Dica: lembre−se que ao
informar o nome o usuário pode digitar letras maiúsculas ou"""

nome = input("Digite o seu nome: ")

nome_maiusculo = nome.upper()

nome_invertido = nome_maiusculo[::-1]

print("Seu nome ao contrário é:", nome_invertido)