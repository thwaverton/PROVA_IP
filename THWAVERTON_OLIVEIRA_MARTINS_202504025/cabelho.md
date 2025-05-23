# PROVA – Introdução à Programação (BIA)
**Nome completo:** THWAVERTON OLIVEIRA MARTINS
**Matrícula:** 202501234
**E-mail institucional:** thwavertonoliveira@discente.ufg.br

## QUESTÃO5
### a)
No nosso projeto, utilizamos o n8n, que é uma plataforma de automação de fluxo de trabalho low-code/no-code. Ele serve para conectar diferentes aplicativos e serviços, permitindo criar lógicas complexas de forma visual, sem a necessidade de escrever muito código. Escolhemos o n8n porque precisávamos integrar várias funcionalidades, como cadastro, login e raspagem de dados,criação de conteudos e roteiros de forma rápida e visual para o desenvolvimento de um agente de IA. A capacidade de criar e testar fluxos complexos rapidamente foi o principal motivo da escolha.
### b)
Uma funcionalidade concreta do projeto construída com o n8n foi o sistema de cadastro e login para um chatbot. Implementamos um fluxo que recebe os dados do usuário (para cadastro ou login) e interage com um banco de dados para verificar as informações. Utilizamos nós (nodes) do tipo "IF" (condicionais) para criar a lógica:

Para cadastro: O fluxo verifica se o e-mail fornecido já existe no banco de dados. Se existir, o cadastro não é permitido e uma mensagem de erro é retornada. Caso contrário, os dados são inseridos.
Para login: O fluxo compara os dados fornecidos com os registros no banco de dados para autenticar o usuário.
Essa funcionalidade foi essencial para controlar o acesso ao agente de IA e foi construída visualmente no n8n, conectando nós de entrada, nós de condição, nós de interação com o banco de dados e nós de resposta.

### c)
Uma funcionalidade que pesquisamos e começamos a desenvolver, mas que ainda não está totalmente implementada, é um fluxo para criar roteiros de conteúdo com base em hashtags (#) ou temas específicos pesquisados em um banco de dados interno. A ideia é que o agente de IA permita ao usuário definir o que ele quer raspar (seja por hashtag, tema, perfil específico ou URL de vídeo do TikTok) e, com base nisso, o n8n iniciaria um fluxo para coletar os dados e depois outro fluxo para processar esses dados e sugerir um roteiro. Já temos a parte de raspagem de dados do TikTok funcionando (usando um fluxo HTTP para interagir com a API da Apify), mas a integração completa disso com a geração automática de roteiros a partir de diferentes tipos de entrada do usuário no agente ainda está em desenvolvimento. A parte do agente que lida com a escolha do tipo de raspagem ainda não está conectada a esse fluxo de geração de roteiros.

## QUESTÃO4
O desenvolvimento do jogo inspirado no Tetris foi o maior desafio da prova. A parte mais difícil foi implementar a detecção de colisão (verificar_colisao) e a rotação das peças, pois precisei garantir que as coordenadas das peças não ultrapassassem os limites do tabuleiro ou se sobrepusessem a blocos fixos. Usei listas aninhadas para representar o tabuleiro e listas de coordenadas para as peças, revisando conceitos de manipulação de listas. Aprendi muito sobre controle de estado e iteração em estruturas de dados complexas.

## QUESTÃO6
Para a questão extra, desenvolvi um minissistema que exibe preços de criptomoedas (Bitcoin, Ethereum e Cardano) em USD e BRL, usando a API CoinGecko (plano Demo, gratuito) e uma interface Tkinter. A interface mostra uma tabela com preços atualizados a cada 60 segundos. Usei a biblioteca requests para acessar o endpoint /simple/price, que é gratuito e suporta até 10.000 chamadas/mês e 30 chamadas/minuto, suficiente para a questão. Tive muita dificuldade para entender como acessar a API, pois buscas na internet não esclareciam como usar o endpoint de forma pública e gratuita. Após várias tentativas, consultei o suporte de IA no site https://docs.coingecko.com/, que forneceu o formato exato da URL.O sistema é simples, mas cumpre o objetivo de exibir dados em tempo real de forma interativa.

## Observações Finais (opcional)
A prova foi bastante desafiadora, especialmente pela necessidade de integrar conceitos de programação estruturada, interfaces gráficas e análise de dados. A questão do Tetris (Q4) exigiu muita lógica para gerenciar o estado do jogo. A questão extra (Q6) me motivou a aprender sobre APIs e Tkinter, o que foi muito desafiador.