# Pedra, papel e tesoura

Este exercício consiste em implementar um jogo de pedra, papel e tesoura de dois jogadores. Você irá precisar fazer uma comparação na função `compareChoices` e retornar uma das três opções "Jogador 1 ganhou!", "Jogador 2 ganhou!", "empate".

## Pseudo código

Este pseudo-código tem o intuito de ajudar a implementar as regras do jogo. Porém ele não é necessário, portanto se quiser pular esta parte não tem problema.

- Início do programa
- Coleta o input do jogador 1
- Coleta o input do jogador 2
- Valida o input sendo "pedra", "papel" ou "tesoura"
- Compara os inputs para definir o vencedor:
  - Pedra ganha de tesoura
  - Tesoura ganha de papel
  - Papel ganha de pedra
- Se o jogador 1 ganhar deve retornar:
  - "Jogador 1 ganhou!"
- Se o jogador 2 ganhar deve retornar:
  - "Jogador 2 ganhou!"
- Se ambos os inputs forem iguais retornar:
  - "empate"

[Regras do Jogo](https://pt.wikipedia.org/wiki/Pedra,_papel_e_tesoura#Regras)

## Desafio

O programa contido no arquivo `game.py` já possui o código para coletar e validar o input dos jogadores, portanto você precisará somente editar a função `compareChoices`

Para executar seu programa basta rodar o comando:
```
python game.py
```

## Rodando os testes

Para rodar os testes basta executar o seguinte comando neste diretório:
```
python test.py
```

