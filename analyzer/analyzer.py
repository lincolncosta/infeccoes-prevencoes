import actionSquares as actionSquares

diceAmount = 1

diceSides = 6
dicePossibilities = range(1, diceSides + 1)

boardSquares = 100
infectionSquares = 18
preventionSquare = 9
luckySquares = 10

diceAvg = sum(dicePossibilities) / diceSides
playsAvg = boardSquares / diceAvg
percentActionSquares = actionSquares.percentCalc(
    boardSquares, infectionSquares + preventionSquare)
percentLuckySquares = actionSquares.percentCalc(
    boardSquares, luckySquares)

# comparação de bifurcações
# zonas de frequência
# quantidade de cartas de perguntas

print('Considerando as seguintes informações:')
print('O jogo será jogado com ' + str(diceAmount) +
      ' dado(s) de ' + str(diceSides) + ' lados e em um tabuleiro de ' + str(boardSquares) + ' casas.')
print('                     ------------------------------')
print('A média de jogadas para que um dos jogadores vença é aproximadamente ' + str(playsAvg) + '.')
print('Os jogadores possuem uma porcentagem de aproximadamente ' +
      str(percentActionSquares * 100) + ' de cair em casas de ação (Infecção e Prevenção), ou seja, cada jogador cai em aproximadamente ' + str(percentActionSquares * playsAvg) + ' casas de ação durante uma partida.')
print('Já para as casas de Sorte, a porcentagem é de aproximadamente ' +
      str(percentLuckySquares * 100) + ', e um jogador cai ' + str(percentLuckySquares * playsAvg) + ' vezes nessas casas durante uma partida.')
