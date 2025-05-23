# **Nome completo:** THWAVERTON OLIVEIRA MARTINS
# **Matrícula:** 202501234
# QUESTÃO 2
import os
import time

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def exibir_cabecalho(titulo):
    limpar_tela()
    print("="*60)
    print(titulo.center(60))
    print("="*60)
    print()

def pausar(mensagem="Aperta ENTER pra continuar..."):
    input(f"\n{mensagem}")

def exibir_menu_principal():
    exibir_cabecalho("SISTEMA DE CONTROLE DE DIN-DIN PESSOAL")

    print("bem-vindo ao teu ajudante financeiro!")
    print("Esse programa vai te ajudar a:")
    print("  • coloca meta pros teus gasto de cada mês")
    print("  • Anota tuas despesa direitinho")
    print("  • Ver se tu tá gastando bão ou se ta estourando a meta")
    print()

    print("Pra começar, tu precisa dizer as categoria dos teus gasto e quanto tu quer gastar em cada uma.")
    print("Exemplo: Comida, Lazer, Transporte, essas coisa aí.")

    pausar()
    return True

# a) O programa deve iniciar solicitando do usuário um conjunto de metas de gastos mensais por categoria.
def coletar_metas():
    metas = {}

    while True:
        exibir_cabecalho("COLOCA AS META DOS GASTO DO MÊS")

        if metas:
            print("Óia as meta que tu ja colocou:")
            for i, (categoria, valor) in enumerate(metas.items(), 1):
                print(f"  {i}. {categoria}: R$ {valor:.2f}")
            print()

        print("E aí, o que tu quer fazer?")
        print("  1. colocar uma categoria nova com meta")
        print("  2. Tá de boa, concluí as meta")

        opcao = input("\nEscolhe uma opção aí (1 ou 2): ")

        if opcao == "1":
            categoria = input("\nDiz o nome da categoria (ex: Comida, Lazer): ").strip()

            if not categoria:
                print("\n   Ó, meu fi, a categoria num pode ficar vazia, não!")
                pausar()
                continue

            if categoria in metas:
                print(f"\n  Essa categoria '{categoria}' já tá na lista, viu?")
                pausar()
                continue

            while True:
                try:
                    valor_texto = input(f"Qual a meta mensal pra '{categoria}' em R$? ")
                    valor = float(valor_texto.replace(',', '.'))

                    if valor <= 0:
                        print("\n  Óia, a meta tem que ser maior que zero, tá?")
                        continue

                    metas[categoria] = valor
                    print(f"\n Beleza, meta pra '{categoria}' ta feita: R$ {valor:.2f}")
                    pausar()
                    break

                except ValueError:
                    print("\n  tem que  coloca um número direitinho!")

        elif opcao == "2":
            if not metas:
                print("\n  Calma ai, tu precisa colocar pelo menos uma categoria!")
                pausar()
                continue

            exibir_cabecalho("RESUMO DAS META QUE TU COLOCOU")
            print("Tuas meta mensal de gasto:")

            for categoria, valor in metas.items():
                print(f"• {categoria}: R$ {valor:.2f}")

            print("\n   Meta tá no jeito!")
            pausar()
            break

        else:
            print("\n  o escolhe direitinho, so 1 ou 2, ta?")
            pausar()

    return metas

# b) Em seguida, o sistema deve solicitar ao usuário o número total de lançamentos financeiros que deseja registrar.
# c) Para cada lançamento, devem ser coletados: descrição, valor e categoria.
def registrar_lancamentos(categorias):
    lancamentos = []

    exibir_cabecalho("ANOTANDO OS GASTO DO MÊS")

    print("Agora vamo anota tuas despesa.")
    print("Pra cada despesa, tu vai dizer:")
    print("  • O que foi (ex: 'Compra na feira')")
    print("  • Quanto custou")
    print("  • Em qual categoria entra")

    while True:
        try:
            num_texto = input("\nquantos gasto tu quer anotar? ")
            num_lancamentos = int(num_texto)

            if num_lancamentos <= 0:
                print("\n  Oia, tem que ser um número maior que zero, viu?")
                continue

            break

        except ValueError:
            print("\n  Meu bem, coloca um número inteiro direitinho!")

    lista_categorias = list(categorias.keys())

    for i in range(1, num_lancamentos + 1):
        exibir_cabecalho(f"GASTO {i} DE {num_lancamentos}")

        while True:
            descricao = input("O que foi essa despesa? ").strip()
            if descricao:
                break
            print("\n  O a descrição num pode ficar vazia, não!")

        while True:
            try:
                valor_texto = input("quanto custou essa despesa em R$? ")
                valor = float(valor_texto.replace(',', '.'))

                if valor <= 0:
                    print("\n  O valor tem que ser maior que zero, meu fi!")
                    continue

                break

            except ValueError:
                print("\n  coloca um numero direitinho, vai!")

        print("\nÓia as categoria que tu tem:")
        for idx, cat in enumerate(lista_categorias, 1):
            print(f"  {idx}. {cat}")

        while True:
            try:
                opcao_texto = input("\nEscolhe o numero da categoria: ")
                opcao = int(opcao_texto)

                if 1 <= opcao <= len(lista_categorias):
                    categoria = lista_categorias[opcao-1]
                    break
                else:
                    print(f"\n  escolhe um numero entre 1 e {len(lista_categorias)}, ta?")

            except ValueError:
                print("\n  , coloca um numero direitinho!")

        lancamento = {
            "descricao": descricao,
            "valor": valor,
            "categoria": categoria
        }
        lancamentos.append(lancamento)

        print(f"\n Gastinho anotado: {descricao} - R$ {valor:.2f} ({categoria})")

        if i < num_lancamentos:
            pausar()


    categorias_com_lancamentos = set(lancamento["categoria"] for lancamento in lancamentos)
    categorias_vazias = [cat for cat in lista_categorias if cat not in categorias_com_lancamentos]

    while categorias_vazias:  
        exibir_cabecalho("CATEGORIAS SEM GASTOS")
        print("Óia, essas categorias tão sem nenhumn gasto registrado:")
        for idx, cat in enumerate(categorias_vazias, 1):
            print(f"  {idx}. {cat}")

        while True:
            resposta = input("\nquer adicionar gastos pra alguma dessas categorias? (s/n),(sim,não): ").strip().lower()
            
            resposta = resposta.replace('ã', 'a').replace('õ', 'o')
            if resposta in ['s', 'sim', 'n', 'nao']:
                break
            print("\n responde com 's', 'sim', 'n' ou 'não', tá?")

        if resposta in ['n', 'nao']:
            break  
        # Perguntar ao usuário qual categoria vazia ele quer preencher
        while True:
            try:
                opcao_texto = input("\nescolhe o número da categoria que tu quer adicionar gastos: ")
                opcao = int(opcao_texto)

                if 1 <= opcao <= len(categorias_vazias):
                    categoria_vazia = categorias_vazias[opcao-1]
                    break
                else:
                    print(f"\n escolhe um número entre 1 e {len(categorias_vazias)}, ta?")

            except ValueError:
                print("\n coloca um numero direitinho!")

        exibir_cabecalho(f"ADICIONANDO GASTOS PARA {categoria_vazia}")
        while True:
            try:
                num_texto = input(f"\nquantos gastos tu quer anotar pra '{categoria_vazia}'? ")
                num_lancamentos_extra = int(num_texto)

                if num_lancamentos_extra <= 0:
                    print("\n Óia tem que ser um numero maior que zero, viu?")
                    continue

                break

            except ValueError:
                print("\n meu bem, coloca um número inteiro direitinho!")

        for i in range(1, num_lancamentos_extra + 1):
            exibir_cabecalho(f"GASTO {i} DE {num_lancamentos_extra} PARA {categoria_vazia}")

            while True:
                descricao = input("o que foi essa despesa? ").strip()
                if descricao:
                    break
                print("\n a descrição num pode ficar vazia, não!")

            while True:
                try:
                    valor_texto = input("Quanto custou essa despesa em R$? ")
                    valor = float(valor_texto.replace(',', '.'))

                    if valor <= 0:
                        print("\n O valor tem que ser maior que zero, meu fi!")
                        continue

                    break

                except ValueError:
                    print("\n coloca um número direitinho, vai!")

            lancamento = {
                "descricao": descricao,
                "valor": valor,
                "categoria": categoria_vazia
            }
            lancamentos.append(lancamento)

            print(f"\n Gastinho anotado: {descricao} - R$ {valor:.2f} ({categoria_vazia})")

            if i < num_lancamentos_extra:
                pausar()

        # lista atualizada 
        categorias_com_lancamentos = set(lancamento["categoria"] for lancamento in lancamentos)
        categorias_vazias = [cat for cat in lista_categorias if cat not in categorias_com_lancamentos]

    print("\n todo os gasto foi anotado direitinho!")
    pausar()

    return lancamentos

# os dados sendo analisado
def analisar_dados(lancamentos, metas):
    exibir_cabecalho("TO OLHANDO TEU DIN-DIN")
    print("perai que tô somando tudo direitinho...")

    for _ in range(3):
        print(".", end="", flush=True)
        time.sleep(0.3)
    print(" Somando os gasto...", end="", flush=True)
    time.sleep(0.5)
    print(" todo certo!")

    for _ in range(3):
        print(".", end="", flush=True)
        time.sleep(0.3)
    print(" vendo as categoria...", end="", flush=True)
    time.sleep(0.5)
    print(" todo certo!")

    for _ in range(3):
        print(".", end="", flush=True)
        time.sleep(0.3)
    print(" comparando com as meta...", end="", flush=True)
    time.sleep(0.5)
    print(" todo certo!")

    estatisticas = {
        "total_despesas": 0,
        "gastos_por_categoria": {},
        "media_por_categoria": {},
        "categoria_maior_gasto": "",
        "valor_maior_gasto": 0,
        "comparativo_metas": {}
    }

    contagem_por_categoria = {}
    for categoria in metas.keys():
        estatisticas["gastos_por_categoria"][categoria] = 0
        contagem_por_categoria[categoria] = 0

    for lancamento in lancamentos:
        valor = lancamento["valor"]
        categoria = lancamento["categoria"]

        estatisticas["total_despesas"] += valor

        if categoria in estatisticas["gastos_por_categoria"]:
            estatisticas["gastos_por_categoria"][categoria] += valor
        else:
            estatisticas["gastos_por_categoria"][categoria] = valor

        if categoria in contagem_por_categoria:
            contagem_por_categoria[categoria] += 1
        else:
            contagem_por_categoria[categoria] = 1

    for categoria, contagem in contagem_por_categoria.items():
        if contagem > 0:
            estatisticas["media_por_categoria"][categoria] = estatisticas["gastos_por_categoria"][categoria] / contagem
        else:
            estatisticas["media_por_categoria"][categoria] = 0

    if estatisticas["gastos_por_categoria"]:
        estatisticas["categoria_maior_gasto"] = max(
            estatisticas["gastos_por_categoria"],
            key=estatisticas["gastos_por_categoria"].get
        )
        estatisticas["valor_maior_gasto"] = estatisticas["gastos_por_categoria"][estatisticas["categoria_maior_gasto"]]

    for categoria, meta in metas.items():
        gasto = estatisticas["gastos_por_categoria"].get(categoria, 0)
        diferenca = meta - gasto
        percentual = (gasto / meta) * 100 if meta > 0 else 0

        if gasto <= meta:
            if percentual >= 90:
                status = "Tá quase no limite"
            else:
                status = "Tá de boa na meta"
        else:
            status = "Passou da meta"

        estatisticas["comparativo_metas"][categoria] = {
            "meta": meta,
            "gasto": gasto,
            "diferenca": diferenca,
            "percentual": percentual,
            "status": status,
        }

    print("\n todo analisado, meu fi!")
    pausar()

    return estatisticas

# d) Geração de relatório com: Total de despesas, Gasto total por categoria,
#    Média de gastos por categoria, Categoria com maior valor gasto,
#    Análise comparativa entre o valor gasto e as metas.
def gerar_relatorio(estatisticas):
    exibir_cabecalho("RELATÓRIO DO TEU DIN-DIN")

    print(" RESUMO GERALZÃO")
    print("-" * 60)
    print(f"total que tu gastou no mes: R$ {estatisticas['total_despesas']:.2f}")

    if estatisticas["categoria_maior_gasto"]:
        print(f"Categoria que tu mais gastou: {estatisticas['categoria_maior_gasto']} "
              f"(R$ {estatisticas['valor_maior_gasto']:.2f})")

    print("\n GASTO POR CATEGORIA")
    print("-" * 60)

    max_valor = max(estatisticas["gastos_por_categoria"].values()) if estatisticas["gastos_por_categoria"] else 0

    for categoria, valor in sorted(
        estatisticas["gastos_por_categoria"].items(),
        key=lambda x: x[1],
        reverse=True
    ):

        print(f"{categoria:<15} R$ {valor:>8.2f} ")

    print("\n MEDIA DOS GASTO POR LANÇAMENTO")
    print("-" * 60)
    for categoria, media in estatisticas["media_por_categoria"].items():
        if media > 0:
            print(f"{categoria:<15} R$ {media:>8.2f} por lançamento")
        else:
            print(f"{categoria:<15} sem gasto nenhum")

    print("\n COMO TU TÁ COM AS META")
    print("-" * 60)
    print(f"{'CATEGORIA':<15} {'META (R$)':<12} {'GASTO (R$)':<12} {'%':>5} {'STATUS':<15}")
    print("-" * 60)

    for categoria, dados in sorted(
        estatisticas["comparativo_metas"].items(),
        key=lambda x: x[1]["percentual"],
        reverse=True
    ):
        meta = dados["meta"]
        gasto = dados["gasto"]
        percentual = dados["percentual"]
        status = dados["status"]

        print(f"{categoria:<15} {meta:<12.2f} {gasto:<12.2f} {percentual:>5.1f}% {status}")

    print("\n UNS CONSELHO PRA TU")
    print("-" * 60)

    categorias_acima = [
        categoria for categoria, dados in estatisticas["comparativo_metas"].items()
        if dados["status"] == "passou da meta"  
    ]

    if categorias_acima:
        print("categoria que tu gastou além da conta:")
        for categoria in categorias_acima:
            dados = estatisticas["comparativo_metas"][categoria]
            excesso = dados["gasto"] - dados["meta"]
            print(f"• {categoria}: Tenta cortar R$ {excesso:.2f} no próximo mês")
    else:
        print(" Arretado! Tu ta dentro da meta em tudo!")

    categorias_proximas = [
        categoria for categoria, dados in estatisticas["comparativo_metas"].items()
        if dados["status"] == "Tá quase no limite"
    ]

    if categorias_proximas:
        print("\ncategoria que tá quase estourando:")
        for categoria in categorias_proximas:
            dados = estatisticas["comparativo_metas"][categoria]
            restante = dados["diferenca"]
            print(f"• {categoria}: Só sobrou R$ {restante:.2f} da meta, óia o cuidado!")

    print("\n" + "="*60)

def exibir_despesas_detalhadas(lancamentos):
    exibir_cabecalho("LISTA DE todo OS TEU GASTO")

    if not lancamentos:
        print("Nenhum gasto anotado ainda")
        pausar()
        return

    print(f"{'#':<4} {'DESCRIÇÃO':<30} {'VALOR (R$)':<15} {'CATEGORIA':<15}")
    print("-" * 60)

    for i, lancamento in enumerate(lancamentos, 1):
        descricao = lancamento["descricao"]
        valor = lancamento["valor"]
        categoria = lancamento["categoria"]

        if len(descricao) > 27:
            descricao = descricao[:24] + "..."

        print(f"{i:<4} {descricao:<30} {valor:<15.2f} {categoria:<15}")

    pausar()

# Menu pra escolher o relatório
def menu_relatorio(estatisticas, lancamentos):
    while True:
        exibir_cabecalho("MENU DOS RELATÓRIO")

        print("Escolhe aí o que tu quer ver:")
        print("  1. Ver o relatório todinho do teu din-din")
        print("  2. Ver a lista detalhada dos gasto")
        print("  3. voltar pro menu principal")

        opcao = input("\ncoloca uma opção (1-3): ")

        if opcao == "1":
            gerar_relatorio(estatisticas)
            pausar()
        elif opcao == "2":
            exibir_despesas_detalhadas(lancamentos)
        elif opcao == "3":
            break
        else:
            print("\n  o, meu bem escolhe entre 1 e 3, tá  ??")
            pausar()

# Função principal que junta tudo
def main():
    exibir_menu_principal()

    metas = coletar_metas()

    lancamentos = registrar_lancamentos(metas)

    estatisticas = analisar_dados(lancamentos, metas)

    menu_relatorio(estatisticas, lancamentos)

    exibir_cabecalho("SISTEMA DE CONTROLE DE DIN-DIN PESSOAL")
    print("valeu por usar nosso sistema!")
    print("\nto torcendo pra essas informação te ajudar a cuidar direitinho do teu din-din.")
    print("\nAté a próxima, viu?")

# Roda o programa
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nOxe, c apertou Ctrl+C? To de boa, programa encerrado!")
    except Exception as e:
        print(f"\n\nEita, deu um erro danado: {e}")
        print("Vou ter que fechar o programa, tá?")