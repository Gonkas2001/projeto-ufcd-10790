from datetime import date 

CALORIAS_POR_SALTO = 0.08

def calculo_imc (peso: float, altura_cm: int) -> float:
    
    altura = altura_cm/100
    imc = float(peso / (altura*altura))
    
    return imc 

def classificacao_imc (imc:float) -> str:
    
        if imc < 18.5:
            return("\n Estás abaixo do peso normal.")
        
        elif imc >= 18.5 and imc < 25:
            return("\n Estás com peso normal.")
        
        elif imc >= 25 and imc <30:
            return("\n Apresentas excesso de peso.")
        
        elif imc >= 30:
            return("\n Apresentas obesidade. Vamos trabalhar!")
        
        
def calcular_calorias(saltos: int) -> float:
    return saltos * CALORIAS_POR_SALTO


def criar_sessao() -> dict:

    saltos = int(input("\nNúmero de saltos realizados: "))
    duracao = int(input("Duração da sessão (minutos): "))

    calorias = calcular_calorias(saltos)

    sessao = {
        "data": str(date.today()),
        "saltos": saltos,
        "duracao": duracao,
        "calorias": calorias
    }

    return sessao       

def mostrar_estatisticas(sessoes: list):

    if len(sessoes) == 0:
        print("\nAinda não existem sessões registadas.")
        return

    total_sessoes = len(sessoes)

    total_saltos = sum(sessao["saltos"] for sessao in sessoes)

    total_calorias = sum(sessao["calorias"] for sessao in sessoes)

    perda_peso = total_calorias / 7700

    print("\n===== ESTATÍSTICAS =====")

    print(f"Total de sessões: {total_sessoes}")
    print(f"Total de saltos: {total_saltos}")
    print(f"Total de calorias gastas: {total_calorias:.2f} kcal")
    print(f"Perda de peso estimada: {perda_peso:.2f} kg")

def program():

    sessoes = []

    nome = input(str("\nOlá, eu sou a tua App dos Saltos! Como te chamas? "))
    peso = float(input(f"\n {nome}, diz-me o teu peso: "))
    altura = int(input("\n Obrigado! E agora a tua altura, em centímetros: "))

    imc = calculo_imc(peso, altura)

    escolha = input(
        f"\n Bem, {nome}, com os dados fornecidos fui capaz de calcular o teu IMC, queres saber? (s/n): "
    ).lower()

    if escolha not in ["s", "sim"]:
        print("\n OK!")

        escolha = input("\n Vamos começar a trabalhar! (s/n ) ").lower()

        if escolha not in ["s", "sim"]:
            return

    if escolha in ["s", "sim"]:
        escolha = input(
            f"\n {nome}, o teu IMC é de {classificacao_imc(imc)}. \n Vamos melhorar esse valor? (s/n) "
        ).lower()

        if escolha not in ["s", "sim"]:
            return

    while True:

        print("\n===== MENU =====")
        print("1 - Registar sessão")
        print("2 - Ver estatísticas")
        print("3 - Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":

            sessao = criar_sessao()

            sessoes.append(sessao)

            print("\nSessão registada com sucesso!")

            print(f"Data: {sessao['data']}")
            print(f"Saltos: {sessao['saltos']}")
            print(f"Duração: {sessao['duracao']} minutos")
            print(f"Calorias: {sessao['calorias']:.2f} kcal")

        elif opcao == "2":

            mostrar_estatisticas(sessoes)

        elif opcao == "3":

            print("\nObrigado por utilizares a App dos Saltos!")
            break

        else:
            print("\nOpção inválida.")

if __name__ == "__main__":
    program()                
        
    
    
