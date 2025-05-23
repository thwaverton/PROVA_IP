# **Nome completo:** THWAVERTON OLIVEIRA MARTINS
# **Matrícula:** 202501234
# QUESTÃO 1
import os
import time

def limpaTela(): 
    os.system('cls' if os.name == 'nt' else 'clear')

def mostraCabecalho(titulo_cab): 
    limpaTela()
    print("="*50)
    print(titulo_cab.center(50))
    print("="*50)
    print()

def daPausa(mensagem="APERTE ENTER PARA CONTINUAR..."): 
    input(f"\n{mensagem}")

def introducao(): 
    mostraCabecalho("CALCULADORA DE LUZ")
    print("Ola, bem-vindo a calculadorra de energia!") 
    print("Para calcular o gasto do seu aparelho, informe o seguinte:") 
    print("  1. A Potensia dele em kilowats (kW).") 
    print("     (Se estiver em Wats (W), tipo '100W', divida por 1000 para virar 0.1kW)") 
    print("  2. Quantas horas por dia, aproximadamente, ele fica ligado.") 
    print("\nInformaremos o consumo do mes em kWh, como na conta de luz. Ok?") 
    daPausa()
# b) Garantir que ambos os valores inseridos sejam positivos e realistas.
def validaEntrada(valorTxt, tipoInfo): 
    try:
        valorFlt = float(valorTxt.replace(',', '.')) 
        if valorFlt <= 0:
            print(f"\n ATENCAO! O valor de '{tipoInfo}' deve ser maior que zero.") 
            return False
        if tipoInfo == "potencia": 
            if valorFlt > 10:
                print(f"\n ATENCAO! Uma potensia de {valorFlt:.1f}kW e muito alta para uma residencia!") 
                print("   Referencia: Geladeira (0.1-0.5kW), Chuveiro (4-7.5kW), Ar Cond. (0.8-2.5kW)") 
                confirmacao = input("   Deseja mesmo continuar com este valor? (s/n): ").strip().lower() 
                return confirmacao == 's'
        elif tipoInfo == "horas":
            if valorFlt > 24:
                print("\n ATENCAO! Um dia so tem 24 horas, o valor nao pode ser maior.") 
                return False
        return True
    except ValueError:
        print(f"\n Ops! O valor de '{tipoInfo}' precisa ser um numero valido. (Ex: 0.5 ou 12)") 
        return False
# c) Criar uma função chamada calcular_consumo_mensal (pot, horas) que realize o cálculo
#    e retorne o consumo mensal estimado.
#    (Nome da função no código: calculaConsumo; Parâmetros: potenciaKw, horasDia)
def calculaConsumo(potenciaKw, horasDia): 
    return potenciaKw * horasDia * 30
# d) Apresentar os resultados de forma clara para o usuário.
def mostraResultado(potKwh, hrsDia, consumoMes): 
    mostraCabecalho("RESULTADO DA CONTA DE LUZ")
    print(f" Potencia do aparelho: {potKwh:.2f} kW") 
    print(f" Tempo ligado por dia: {hrsDia:.1f} horas") 
    print("-" * 50)
    print(f" Consumo estimado no mes: {consumoMes:.2f} kWh") 
    print("-" * 50)
    
    msg_consumo = " Consumo esta normal." 
    if consumoMes >= 300:
        msg_consumo = " ATENCAO! Este consumo esta muito alto. Verifique o aparelho." 
    elif consumoMes >= 100:
        msg_consumo = " Cuidado. Este consumo pode pesar no seu orcamento." 
    elif consumoMes >= 30:
        msg_consumo = " Consumo moderado." 
    print(f"\n{msg_consumo}")

primeiraVezExecucao = True

def programaPrincipal(): 
    global primeiraVezExecucao 
    introducao()
    rodando = True
    while rodando:
        mostraCabecalho("CALCULADORA DE LUZ")
        if not primeiraVezExecucao:
             print("Vamos calcular novamente!") 
        primeiraVezExecucao = False
        # a) Solicitar ao usuário dois valores: potência e tempo de uso.
        while True:
            textoPotencia = input("\n Potencia do aparelho em kW (ex: 0.5 ou 1,2): ").strip() 
            if validaEntrada(textoPotencia, "potencia"): 
                break
            daPausa("APERTE ENTER PARA TENTAR A POTENCIA NOVAMENTE...") 
        
        mostraCabecalho("CALCULADORA DE LUZ")
        print(f" Potencia informada: {textoPotencia.replace('.',',')} kW") 

        while True:
            textoHoras = input("\n Quantas horas por dia o aparelho fica ligado (ex: 8 ou 12.5): ").strip() 
            if validaEntrada(textoHoras, "horas"):
                break
            daPausa("APERTE ENTER PARA TENTAR AS HORAS NOVAMENTE...")

        limpaTela()
        print("Calculando, por favor aguarde um momento...") 
        for _ in range(4): 
            print(" .", end="", flush=True)
            time.sleep(0.25)
        print(" Pronto!")
        print()

        potFinal = float(textoPotencia.replace(',', '.')) 
        horasFinal = float(textoHoras.replace(',', '.')) 

        consumoTotal = calculaConsumo(potFinal, horasFinal) 
        mostraResultado(potFinal, horasFinal, consumoTotal)

        print("-" * 50)
        if input("\nDeseja calcular de outro aparelho? (s/n): ").strip().lower() != 's': 
            rodando = False
            
    mostraCabecalho("CALCULADORA DE LUZ")
    print("\nObrigado por usar a calculadora! Esperamos que tenha sido util!") 
    print("Volte sempre que precisar!") 

if __name__ == "__main__":
    try:
        programaPrincipal()
    except KeyboardInterrupt:
        print("\n\nVoce pressionou CTRL+C? Programa encerrado. Volte sempre!") 
    except Exception as err_ex: 
        print(f"\n\nOcorreu um problema inesperado: {err_ex}") 
        print("Sugerimos fechar e tentar novamente mais tarde.")