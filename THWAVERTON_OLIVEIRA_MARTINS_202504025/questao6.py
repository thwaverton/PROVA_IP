# **Nome completo:** THWAVERTON OLIVEIRA MARTINS
# **Matrícula:** 202501234
# QUESTÃO 5
import tkinter as tk
import requests
import time

IDS_CRIPTOS = ['bitcoin', 'ethereum', 'cardano']
MOEDAS_PARA_VER = ['usd', 'brl']
TEMPO_ATUALIZAR_SEGUNDOS = 60

def buscar_precos_cripto(lista_ids_criptos, lista_moedas_cotacao):
    param_ids = ",".join(lista_ids_criptos)
    param_moedas = ",".join(lista_moedas_cotacao)
    url_api = f"https://api.coingecko.com/api/v3/simple/price?ids={param_ids}&vs_currencies={param_moedas}"
    
    try:
        resp = requests.get(url_api, timeout=10)
        resp.raise_for_status()
        dados = resp.json()
        return dados
    except :
        print(f"Eita, erro lascou tudo skksksksks")
    return None

class PainelCriptoApp:
     # Configura a janela principal e inicializa variáveis de controle da interface.
    def __init__(self, janela_principal):
        self.janela = janela_principal
        self.janela.title("Painel de Criptos")
        self.janela.geometry("400x280")

        self.msg_status = tk.StringVar(value="Carregando moedas...")
        self.texto_ultima_att = tk.StringVar(value="Atualizado em: --:--:--")
        
        self.vars_precos = {}
        for id_cripto in IDS_CRIPTOS:
            self.vars_precos[id_cripto] = {}
            for moeda_cotacao in MOEDAS_PARA_VER:
                self.vars_precos[id_cripto][moeda_cotacao] = tk.StringVar(value="--.--")

        self._montar_interface_grafica()
        self.atualizar_precos_na_tela()

    def _montar_interface_grafica(self):
        label_titulo = tk.Label(self.janela, text="Painel de Criptomoedas", font=("Arial", 16, "bold"), pady=10)
        label_titulo.grid(row=0, column=0, columnspan=len(MOEDAS_PARA_VER) + 1, sticky="ew")

        tk.Label(self.janela, text="Criptomoeda", font=("Arial", 10, "bold"), padx=5, pady=5).grid(row=1, column=0, sticky="w")
        for i, moeda_cotacao in enumerate(MOEDAS_PARA_VER):
            tk.Label(self.janela, text=moeda_cotacao.upper(), font=("Arial", 10, "bold"), padx=5, pady=5).grid(row=1, column=i + 1, sticky="w")

        linha_atual = 2
        for id_cripto in IDS_CRIPTOS:
            tk.Label(self.janela, text=id_cripto.capitalize(), font=("Arial", 10), padx=5, pady=3, anchor="w").grid(row=linha_atual, column=0, sticky="ew")
            for i, moeda_cotacao in enumerate(MOEDAS_PARA_VER):
                label_preco = tk.Label(self.janela, textvariable=self.vars_precos[id_cripto][moeda_cotacao], font=("Arial", 10), padx=5, pady=3, anchor="w")
                label_preco.grid(row=linha_atual, column=i + 1, sticky="ew")
            linha_atual += 1

        label_ultima_att = tk.Label(self.janela, textvariable=self.texto_ultima_att, font=("Arial", 8), pady=5)
        label_ultima_att.grid(row=linha_atual, column=0, columnspan=len(MOEDAS_PARA_VER) + 1, sticky="ew", pady=(10,0))
        linha_atual += 1

        label_status = tk.Label(self.janela, textvariable=self.msg_status, font=("Arial", 8), pady=5)
        label_status.grid(row=linha_atual, column=0, columnspan=len(MOEDAS_PARA_VER) + 1, sticky="ew")
        
        self.janela.grid_columnconfigure(0, weight=2)
        for i in range(len(MOEDAS_PARA_VER)):
            self.janela.grid_columnconfigure(i+1, weight=1)

    def atualizar_precos_na_tela(self):
        self.msg_status.set("buscando precos novos...")
        
        dados_buscados = buscar_precos_cripto(IDS_CRIPTOS, MOEDAS_PARA_VER)
        
        if dados_buscados:
            self.texto_ultima_att.set(f"atualizado em: {time.strftime('%H:%M:%S')}")
            for id_cripto in IDS_CRIPTOS:
                if id_cripto in dados_buscados:
                    for moeda_cotacao in MOEDAS_PARA_VER:
                        if moeda_cotacao in dados_buscados[id_cripto]:
                            preco = dados_buscados[id_cripto][moeda_cotacao]
                            self.vars_precos[id_cripto][moeda_cotacao].set(f"{preco:,.2f}")
                        else:
                            self.vars_precos[id_cripto][moeda_cotacao].set("N/D") 
                else:
                    for moeda_cotacao in MOEDAS_PARA_VER:
                         self.vars_precos[id_cripto][moeda_cotacao].set("erro!")
            self.msg_status.set("Preços na tela!")
        else:
            self.msg_status.set("Ih, falhou em buscar. tentando de novo daqui a pouco...")
            for id_cripto in IDS_CRIPTOS:
                 for moeda_cotacao in MOEDAS_PARA_VER:
                    self.vars_precos[id_cripto][moeda_cotacao].set("falhou")

        self.janela.after(TEMPO_ATUALIZAR_SEGUNDOS * 1000, self.atualizar_precos_na_tela)

if __name__ == "__main__":
    janela_principal_tk = tk.Tk()
    meu_app_cripto = PainelCriptoApp(janela_principal_tk)
    janela_principal_tk.mainloop()

