# **Nome completo:** THWAVERTON OLIVEIRA MARTINS
# **Matrícula:** 202501234
# QUESTÃO 4
import random
import os
import time

LARGURA_T = 10
ALTURA_T = 20
VAZIO = '.'
BLOCO_PECA_ATUAL = 'O'
BLOCO_FIXO = '#'

PECAS = [
    # Peça "I" (a barra reta)
    [
        [(0,0), (0,1), (0,2), (0,3)],  # rotação 1 (horizontal)
        [(0,0), (1,0), (2,0), (3,0)]   # rotação 2 (vertical)
    ],

    # Peça "O" (o quadrado)
    [
        [(0,0), (0,1), (1,0), (1,1)]   # rotação 1 (forma de bloco/quadrado)
    ],

    # Peça "T"
    [
        [(0,0), (0,1), (0,2), (1,1)],  # rotação 1 (horizontal, "T" normal)
        [(0,0), (1,0), (2,0), (1,1)],  # rotação 2 (vertical, "T" deitado para direita)
        [(1,0), (0,1), (1,1), (2,1)],  # rotação 3 (horizontal, "T" invertido)
        [(1,0), (0,1), (1,1), (1,2)]   # rotação 4 (vertical, "T" deitado para esquerda)
    ],

    # Peça "L" (a forma de L tradicional)
    [
        [(0,0), (1,0), (2,0), (2,1)],  # rotação 1 (vertical, pé para direita)
        [(0,0), (0,1), (0,2), (1,0)],  # rotação 2 (horizontal, pé para baixo)
        [(0,0), (0,1), (1,1), (2,1)],  # rotação 3 (vertical, pé para esquerda)
        [(1,0), (1,1), (1,2), (0,2)]   # rotação 4 (horizontal, pé para cima)
    ],

    # Peça "J" 
    [
        [(0,1), (1,1), (2,1), (2,0)],  # rotação 1 (formato J com pé para esquerda)
        [(0,2), (1,2), (2,2), (2,1)],  # rotação 2 (formato J com pé para esquerda, deslocado)
        [(0,0), (1,0), (2,0), (0,1)],  # rotação 3 (formato L com pé para direita)
        [(0,0), (1,0), (2,0), (2,1)]   # rotação 4 (formato L com pé para direita)
    ],
    # Peça "S"
    [
        [(1,0), (2,0), (0,1), (1,1)],  # rotação 1 (orientação vertical, "S em pé")
        [(0,0), (0,1), (1,1), (1,2)]   # rotação 2 (orientação horizontal, "S deitado")
    ],
    # Peça "Z"
    [
        [(0,0), (1,0), (1,1), (2,1)],  # rotação 1 (orientação vertical, "Z em pé")
        [(1,0), (0,1), (1,1), (0,2)]   # rotação 2 (orientação horizontal, "Z deitado")
    ]
]

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def criar_tabuleiro():
     # Cria matriz (lista de listas) representando o tabuleiro vazio.
    return [[VAZIO for _ in range(LARGURA_T)] for _ in range(ALTURA_T)]

def nova_peca():
     # Escolhe tipo aleatório de peça e define sua posição/rotação inicial.
    tipo_peca = random.randrange(len(PECAS))
    return tipo_peca, 0, LARGURA_T // 2 - 2, 0

def verificar_colisao(tabuleiro, tipo_peca_idx, rot_idx, px, py):
    # Checa se a peça na nova posição/rotação bate nas bordas ou em blocos.
    forma_peca = PECAS[tipo_peca_idx][rot_idx]
    for dy, dx in forma_peca:
        y_abs, x_abs = py + dy, px + dx
        if not (0 <= x_abs < LARGURA_T and 0 <= y_abs < ALTURA_T and \
                tabuleiro[y_abs][x_abs] == VAZIO):
            return True
    return False

def fixar_peca(tabuleiro, tipo_peca_idx, rot_idx, px, py):
    # Torna os blocos da peça atual parte fixa do tabuleiro.
    forma_peca = PECAS[tipo_peca_idx][rot_idx]
    for dy, dx in forma_peca:
        y_abs, x_abs = py + dy, px + dx
        if 0 <= y_abs < ALTURA_T and 0 <= x_abs < LARGURA_T:
            tabuleiro[y_abs][x_abs] = BLOCO_FIXO

def eliminar_linhas_completas(tabuleiro):
    linhas_eliminadas = 0
    y_tab = ALTURA_T - 1
    while y_tab >= 0:
        if VAZIO not in tabuleiro[y_tab]:
            del tabuleiro[y_tab]
            tabuleiro.insert(0, [VAZIO for _ in range(LARGURA_T)])
            linhas_eliminadas += 1
        else:
            y_tab -= 1
    return linhas_eliminadas

def desenhar_tela(tabuleiro, peca_info_atual, pontuacao):
    limpar_tela()
    tab_temp = [linha[:] for linha in tabuleiro]

    if peca_info_atual:
        tipo_idx, rot_idx, px, py = peca_info_atual
        forma_peca = PECAS[tipo_idx][rot_idx]
        for dy, dx in forma_peca:
            y_abs, x_abs = py + dy, px + dx
            if 0 <= y_abs < ALTURA_T and 0 <= x_abs < LARGURA_T:
                tab_temp[y_abs][x_abs] = BLOCO_PECA_ATUAL

    print("--- TETRIS SIMPLES ---")
    for y in range(ALTURA_T):
        print("|" + "".join(tab_temp[y]) + "|")
    print("+" + "-" * LARGURA_T + "+")
    print(f"Pontos: {pontuacao}")
    print("Acoes: a(esq), d(dir), w(rot), s(baixo), q(sair)") 

def loop_jogo():
    tabuleiro = criar_tabuleiro()
    peca_idx_atual, rot_idx_atual, px_atual, py_atual = nova_peca()
    pontuacao = 0
    fim_de_jogo = False
    intervalo_queda = 0.7
    ultimo_tempo_queda = time.time()

    while not fim_de_jogo:
        desenhar_tela(tabuleiro, (peca_idx_atual, rot_idx_atual, px_atual, py_atual), pontuacao)

        acao = input("Acao: ").lower()

        novo_px, novo_py, nova_rot = px_atual, py_atual, rot_idx_atual

        if acao == 'q':
            fim_de_jogo = True
            continue
        elif acao == 'a':
            novo_px -= 1
        elif acao == 'd':
            novo_px += 1
        elif acao == 'w': 
            nova_rot = (rot_idx_atual + 1) % len(PECAS[peca_idx_atual])

        if acao in ['a', 'd', 'w']: 
            if not verificar_colisao(tabuleiro, peca_idx_atual, nova_rot, novo_px, py_atual):
                px_atual, rot_idx_atual = novo_px, nova_rot

        if acao == 's' or (time.time() - ultimo_tempo_queda > intervalo_queda):
            if not verificar_colisao(tabuleiro, peca_idx_atual, rot_idx_atual, px_atual, py_atual + 1):
                py_atual += 1
                if acao == 's': pontuacao += 1
            else:
                fixar_peca(tabuleiro, peca_idx_atual, rot_idx_atual, px_atual, py_atual)
                linhas_limpas = eliminar_linhas_completas(tabuleiro)
                if linhas_limpas > 0:
                    pontuacao += (linhas_limpas ** 2) * 100

                peca_idx_atual, rot_idx_atual, px_atual, py_atual = nova_peca()
                if verificar_colisao(tabuleiro, peca_idx_atual, rot_idx_atual, px_atual, py_atual):
                    fim_de_jogo = True
            ultimo_tempo_queda = time.time()

    limpar_tela()
    desenhar_tela(tabuleiro, None, pontuacao)
    print("\n!!! FIM DE JOGO !!!")
    print(f"Pontuaçao final: {pontuacao}")

if __name__ == "__main__":
    loop_jogo()