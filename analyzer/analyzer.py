diceAmount = 1

diceSides = 6
dicePossibilities = range(1, diceSides + 1)

boardSquares = 100
# luckySquares = 10

diceAvg = sum(dicePossibilities) / diceSides
playsAvg = boardSquares / diceAvg 

# comparação de bifurcações
# zonas de frequência
# quantidade de cartas de perguntas

print('Considerando as seguintes informações:')
print('O jogo será jogado com ' + str(diceAmount) +
      ' dado(s) de ' + str(diceSides) + ' lados e em um tabuleiro de ' + str(boardSquares) + ' casas.')
print('A média de jogadas para que um dos jogadores vença é: ', str(playsAvg))
