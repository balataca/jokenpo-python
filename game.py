def compareChoices(player1, player2):
    """
    ATENÇÃO: Escreva seu código aqui
    Você deve comparar os inputs dos dois jogadores e retornar uma das três opções:
    1. "Jogador 1 ganhou!"
    2. "Jogador 2 ganhou!"
    3. "empate"   
    """
    return "empate"

def validateInput(player1, player2):
    validChoices = ["pedra", "papel", "tesoura"]
    isPlayer1Valid = player1 in validChoices
    isPlayer2Valid = player2 in validChoices
    
    if not isPlayer1Valid:
        print("Escolha do jogador 1 invalida")
    if not isPlayer2Valid:
        print("Escolha do jogador 2 invalida")
    if isPlayer1Valid and isPlayer2Valid:
        result = compareChoices(player1, player2)
        print(result)

def startGame():
    print('Jogador 1:')
    player1 = input()
    print('Jogador 2:')
    player2 = input()
    validateInput(player1, player2)