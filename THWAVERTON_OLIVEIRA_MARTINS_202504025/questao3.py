# **Nome completo:** THWAVERTON OLIVEIRA MARTINS
# **Matrícula:** 202501234
# QUESTÃO 3
import pandas as pd
import numpy as np
import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def exibir_cabecalho(titulo):
    limpar_tela()
    print("="*70)
    print(titulo.center(70))
    print("="*70)

def pausar(mensagem="aperte enter..."):
    input(f"\n{mensagem}")

def gerar_dados_iniciais_se_necessario(nome_arquivo_csv):
    if not os.path.exists(nome_arquivo_csv):
        exibir_cabecalho("geracao de dados iniciais")
        print(f"arquivo '{nome_arquivo_csv}' nao encontrado.")
        print("gerando novos dados de temperatura para 30 dias...")

        np.random.seed(42)
        temperaturas_geradas = np.random.uniform(low=10.0, high=38.0, size=30)
        temperaturas_geradas = np.round(temperaturas_geradas, 1)
        dias_do_mes = np.arange(1, 31)

        df_novo = pd.DataFrame({
            'Dia': dias_do_mes,
            'Temperatura_Celcius': temperaturas_geradas
        })

        try:
            df_novo.to_csv(nome_arquivo_csv, index=False)
            print(f"\nArquivo '{nome_arquivo_csv}' criado!")
            print("metodo de geraçao: 30 temperaturas aleatórias (entre 10.0°C e 38.0°C, uma casa decimal).")
            print("dados gerados (Temperatura_Celcius):")
            print(list(temperaturas_geradas))
        except Exception as e:
            print(f"\nocorreu um erro ao tentar salvar o arquivo '{nome_arquivo_csv}': {e}")
            print("o programa pode não funcionar corretamente sem o arquivo de dados.")
        pausar("ressione ENTER para continuar com o carregamento dos dados...")
    else:
        print(f"Arquivo de dados '{nome_arquivo_csv}' encontrado. usando dados existentes.")

def carregar_dados_do_csv(nome_arquivo="temperaturas_diarias.csv"):
    exibir_cabecalho("abrindo csv")
    print(f"tentando abrir o arquivo '{nome_arquivo}'...")

    try:
        df_temperaturas = pd.read_csv(nome_arquivo)
        print("ok, arquivo lido.")

        if 'Dia' not in df_temperaturas.columns or 'Temperatura_Celcius' not in df_temperaturas.columns:
            print("\nxi, faltam colunas 'dia' ou 'temperatura_celcius' no arquivo.")
            print("   veja o arquivo. programa vai fechar.")
            input("\nenter para sair.")
            exit()

        print("\ndados carregados (inicio):")
        print(df_temperaturas.head())

    except FileNotFoundError:
        print(f"\nO arquivo '{nome_arquivo}'ao foi encontrado ou nao pode ser criado.")
        print("   sem ele, nao e possivel rodar. programa fechando.")
        input("\nenter para sair.")
        exit()
    except Exception as e:
        print(f"\nerro ao ler o arquivo '{nome_arquivo}': {e}")
        print("   deu ruim. programa fechando.")
        input("\nenter para sair.")
        exit()

    pausar()
    return df_temperaturas
# a) Use o NumPy para calcular: média, mediana, desvio padrão, índice de variação térmica média.
def calcular_estatistica(lista_de_temperaturas):
    exibir_cabecalho("calculos estatisticos")
    array_temps = np.array(lista_de_temperaturas)

    print("calculando...")

    media_mensal = np.mean(array_temps)
    mediana_mensal = np.median(array_temps)
    desvio_padrao = np.std(array_temps)

    diferencas_abs = np.abs(array_temps - media_mensal)
    indice_variacao = np.mean(diferencas_abs)

    print("feito.\n")

    print("estatisticas do mes:")
    print("-"*60)
    print(f"temperatura media mensal: {media_mensal:.2f} °c")
    print(f"mediana das temperaturas: {mediana_mensal:.2f} °c")
    print(f"desvio padrao das temperaturas: {desvio_padrao:.2f} °c")
    print(f"indice de variacao termica media: {indice_variacao:.2f} °c")
    print("-"*60)

    pausar()
    return media_mensal
# b) Crie um DataFrame do Pandas com: Dia do mês, Temperatura média do dia, "Diferença para a média".
# c) Crie uma nova coluna no DataFrame chamada "Classificação térmica".
def FRAME_DADOS(df_dados, media_do_mes_calculada):
    exibir_cabecalho("mexendo na tabela")

    df_processado = df_dados.copy()

    df_processado['Diferenca_Para_Media'] = df_processado['Temperatura_Celcius'] - media_do_mes_calculada

    classificacoes = []
    for temp in df_processado['Temperatura_Celcius']:
        if temp < 18:
            classificacoes.append("frio")
        elif temp >= 18 and temp <= 25:
            classificacoes.append("agradavel")
        else:
            classificacoes.append("quente")

    df_processado['Classificacao_Termica'] = classificacoes

    print("\ntabela atualizada (inicio):")
    print(df_processado.head())

    pausar()
    return df_processado

# d) Ao final, apresente os seguintes resultados:
#    i. Conte o número total de dias classificados.
#    ii. Exiba os 5 dias mais quentes e os 5 dias mais frios.
#    iii. Para cada um desses 10 dias, cruze a classificação térmica com a diferença para a média.
#    iv. Responda: Houve dias "Frio" acima da média? Houve dias "Quente" abaixo da média?
def RELATORIO_CLIMA(df_completo, media_mensal_arredondada):
    exibir_cabecalho("relatorio do mes")

    print("1. resumo classificacao:")
    contagem_classificacao = df_completo['Classificacao_Termica'].value_counts()
    for tipo_clima, quantidade in contagem_classificacao.items():
        print(f"   - {tipo_clima}: {quantidade} dias")
    print("-"*60)
    pausar("enter para dias extremos...")

    print("\n2. dias mais quentes/frios:")
    dias_quentes = df_completo.nlargest(5, 'Temperatura_Celcius')
    dias_frios = df_completo.nsmallest(5, 'Temperatura_Celcius')

    print("\n   top 5 quentes:")
    for indice, dados_dia in dias_quentes.iterrows():
        print(f"      - dia {dados_dia['Dia']}: {dados_dia['Temperatura_Celcius']:.1f}°c ({dados_dia['Classificacao_Termica']})")

    print("\n   top 5 frios:")
    for indice, dados_dia in dias_frios.iterrows():
        print(f"      - dia {dados_dia['Dia']}: {dados_dia['Temperatura_Celcius']:.1f}°c ({dados_dia['Classificacao_Termica']})")
    print("-"*60)
    pausar("enter para analise 10 dias...")

    print(f"\n3. analise 10 dias (media: {media_mensal_arredondada:.1f}°c):")

    dias_extremos = pd.concat([dias_quentes, dias_frios])

    print(f"{'dia':<5} | {'temp.':<7} | {'classif.':<10} | {'diferenca p/ media':<18} | {'relacao c/ media'}")
    print("-"*60)
    for indice, dados_dia in dias_extremos.iterrows():
        dif_formatada = f"{dados_dia['Diferenca_Para_Media']:.1f}°C"
        relacao_media = ""
        if dados_dia['Diferenca_Para_Media'] > 0.05:
            relacao_media = "acima"
        elif dados_dia['Diferenca_Para_Media'] < -0.05:
            relacao_media = "abaixo"
        else:
            relacao_media = "na media"

        print(f"{dados_dia['Dia']:<5} | {dados_dia['Temperatura_Celcius']:<7.1f} | {dados_dia['Classificacao_Termica']:<10} | {dif_formatada:<20} | {relacao_media}")
    print("-"*60)
    pausar("enter para finalizar...")


    frio_acima_media = df_completo[
        (df_completo['Classificacao_Termica'] == 'frio') &
        (df_completo['Diferenca_Para_Media'] > 0)
    ]
    if not frio_acima_media.empty:
        print(f"   - sim, {len(frio_acima_media)} dia(s) 'frio' acima da media ({media_mensal_arredondada:.1f}°c).")
        for _, dia_especifico in frio_acima_media.iterrows():
            print(f"     - d{dia_especifico['Dia']}: {dia_especifico['Temperatura_Celcius']:.1f}°c")
    else:
        print(f"   - não, nenhum 'frio' acima da media ({media_mensal_arredondada:.1f}°c).")

    quente_abaixo_media = df_completo[
        (df_completo['Classificacao_Termica'] == 'quente') &
        (df_completo['Diferenca_Para_Media'] < 0)
    ]
    if not quente_abaixo_media.empty:
        print(f"\n   - sim, {len(quente_abaixo_media)} dia(s) 'quente' abaixo da media ({media_mensal_arredondada:.1f}°c).")
        for _, dia_especifico in quente_abaixo_media.iterrows():
             print(f"     - d{dia_especifico['Dia']}: {dia_especifico['Temperatura_Celcius']:.1f}°c")
    else:
        print(f"\n   - nao, nenhum 'quente' abaixo da media ({media_mensal_arredondada:.1f}°c).")
    print("-"*60)

def main():
    nome_do_arquivo_csv = "temperaturas_diarias.csv"

    exibir_cabecalho("analise de clima")
    print("ola. programa para analisar temperaturas do mes.")
    print(f"usara o arquivo '{nome_do_arquivo_csv}'.")

    gerar_dados_iniciais_se_necessario(nome_do_arquivo_csv)
    pausar("Pressione ENTER para carregar os dados e iniciar a analise...")


    dataframe_temperaturas = carregar_dados_do_csv(nome_do_arquivo_csv)

    temperaturas_para_numpy = dataframe_temperaturas['Temperatura_Celcius'].tolist()

    media_calculada = calcular_estatistica(temperaturas_para_numpy)

    dataframe_analisado = FRAME_DADOS(dataframe_temperaturas, media_calculada)

    RELATORIO_CLIMA(dataframe_analisado, media_calculada)

    exibir_cabecalho("fim da analise")
    print("pronto, terminou.")
    print("espero que tenha sido util.")
    print("rode de novo ou veja o codigo se precisar.")
    print("tchau!")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        limpar_tela()
        print("\n\ninterrompido. saindo.")
    except Exception as erro_inesperado:
        limpar_tela()
        print("\n\nops! erro inesperado:")
        print(erro_inesperado)
        print("   deu ruim. avise alguem. saindo.")