# Tabuleiro de Números  

Este projeto foi desenvolvido como avaliação da disciplina **MI Algoritmos I – EXA854**.  

O produto solicitado foi um **jogo de tabuleiro em Python**, inspirado em um desafio da liga de jogos do IEEE UEFS. O sistema consiste em um tabuleiro de dimensão variável (N x N), no qual dois jogadores se alternam colocando números até que um deles complete a sequência sorteada no início da partida.  

O jogo implementa funcionalidades que o tornam mais atrativo e dinâmico, como ranking de vitórias, jogada especial e diferenciação visual entre os jogadores.  

## Funcionalidades  

- **Tabuleiro dinâmico**: disponível em três níveis de dificuldade (3x3, 4x4 e 5x5).  
- **Objetivos sorteados**: cada jogador recebe uma sequência aleatória (ascendente, descendente, pares ou ímpares) que deve ser completada em linha, coluna ou diagonal.  
- **Turnos alternados**: os jogadores realizam jogadas no mesmo computador, com ordem de início embaralhada automaticamente.  
- **Jogada especial**: possibilidade de limpar uma linha ou coluna antes de realizar uma jogada normal.  
- **Ranking de vitórias**: registro em arquivo das vitórias dos jogadores, exibindo os 10 melhores colocados.  
- **Interface em modo texto**: tabuleiro exibido de forma organizada no terminal, com diferenciação de cores para cada jogador.  
- **Validação de entradas**: apenas comandos válidos são aceitos, garantindo maior robustez.  

## Limitações  

- A opção de **carregar partidas salvas** não foi implementada nesta versão.  
- O sistema ainda pode ser expandido com novos recursos, como tabuleiros maiores e mais habilidades especiais.  
