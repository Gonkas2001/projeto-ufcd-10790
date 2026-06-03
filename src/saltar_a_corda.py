from datetime import date 

date = date.today().year

def calculo_imc (peso: float, altura_cm: int) -> float:
    
    altura = altura_cm/100
    imc = float(peso / (altura*altura))
    
    return imc 

def classificacao_imc (imc:float) -> str:
    
        if imc < 18.5:
            return("\n Estás abaixo do peso normal.")
        
        elif imc >= 18.5 and imc < 25:
            return("\n Estás com peso normal.")
        
        elif imc > 25 and imc <30:
            return("\n Apresentas excesso de peso.")
        
        elif imc >= 30:
            return("\n Apresentas obesidade. Vamos trabalhar!")
        
def program ():
    
while True:
    
    nome=input(str("\nOlá, eu sou a tua App dos Saltos! Como te chamas? "))
    peso=float(input(f"\n {nome}, diz-me o teu peso: "))
    altura=int(input("\n Obrigado! E agora a tua altura, em centímetros: "))

    imc = calculo_imc(peso, altura)
    
    escolha = input(int(f"\n Bem, {nome}, com os dados fornecidos fui capaz de calcular o teu IMC, queres saber? (s/n): ")).lower()
    
    if escolha not in ["s", "sim"]:
        print("\n OK!"),
           
        escolha = input("\n Vamos começar a trabalhar! (s/n ) ").lower()   
        if escolha not in ["s", "sim"]:
            break
    
    if escolha in ["s", "sim"]:
        escolha = input(f"\n {nome}, o teu IMC é de {classificacao_imc(imc)}. \n Vamos melhorar esse valor? (s/n) ").lower()
            
        if escolha not in ["s", "sim"]:
            break
    
    
        
        
    
    
