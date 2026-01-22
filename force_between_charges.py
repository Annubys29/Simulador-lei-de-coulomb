import matplotlib
import numpy
import math

K = 8.99e9

def calcular_forca():
    q1 = float(input("Digite q1 (C): "))
    q2 = float(input("Digite q2 (C): "))
    r = float(input("Digite a Distância (m):"))
    F = K*(q1*q2) / (r**2)
    print("Força =", F, "N")

def calcular_distancia():
    q1 = float(input("Digite q1 (C):"))
    q2 = float(input("Digite q2 (C):"))
    F = float(input("Digite a força (N)"))
    r = math.sqrt((K*q1*q2)/F)

def calcular_carga_q1():
    q2 = float(input("Digite q2 (C): "))
    r = float(input("Digite a distância (m): "))
    F = float(input("Digite a força (N): "))
    q1 = (F*r**2)/(K*q2)

def calcular_carga_q2():
    q1 = float(input("Digite q1 (C): "))
    r = float (input("Digite a distância (m)"))
    F = float(input("Digite a força (N): "))
    q2 = (F*r**2)/(K*q1)

def menu():
    print("\n===Simulador da Lei de Coulomb ===")
    print("1 - Calcular Força")
    print("2 - Calcular Distância")
    print("3 - Calcular q1")
    print("4 - Calcular q2")

def main():
    while True:
        menu()
        opcao = input("Escolha uma das opções(ou zero para sair): ")

        if opcao == "1":
            calcular_forca()
        elif opcao == "2":
            calcular_distancia()
        elif opcao == "3":
            calcular_carga_q1
        elif opcao == "4":
            calcular_carga_q2
        elif opcao == "0":
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
