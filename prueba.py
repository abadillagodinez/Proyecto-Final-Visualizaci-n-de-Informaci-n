import pandas as pd
dataMatches = pd.read_csv("./Data/matches2020.csv")
champ = "Vi"

winCant = 0
for index in dataMatches.index:
    rTop = dataMatches["redtop"][index]
    rJg = dataMatches["redjungle"][index]
    rMid = dataMatches["redmid"][index]
    rAdc = dataMatches["redadc"][index]
    rSupp = dataMatches["redsupport"][index]
    bTop = dataMatches["bluetop"][index]
    bJg = dataMatches["bluejungle"][index]
    bMid = dataMatches["bluemid"][index]
    bAdc = dataMatches["blueadc"][index]
    bSupp = dataMatches["bluesupport"][index]
    win = dataMatches["result"][index]
    if (champ == rTop or champ == rJg or champ == rMid or champ == rAdc or champ == rSupp) and (win == 0):
        winCant = winCant + 1
    elif (champ == bTop or champ == bJg or champ == bMid or champ == bAdc or champ == bSupp) and (win == 1):
        winCant = winCant + 1

pickCant = 0
for index in dataMatches.index:
    rTop = dataMatches["redtop"][index]
    rJg = dataMatches["redjungle"][index]
    rMid = dataMatches["redmid"][index]
    rAdc = dataMatches["redadc"][index]
    rSupp = dataMatches["redsupport"][index]
    bTop = dataMatches["bluetop"][index]
    bJg = dataMatches["bluejungle"][index]
    bMid = dataMatches["bluemid"][index]
    bAdc = dataMatches["blueadc"][index]
    bSupp = dataMatches["bluesupport"][index]
    win = dataMatches["result"][index]
    if (champ == rTop or champ == rJg or champ == rMid or champ == rAdc or champ == rSupp or champ == bTop or champ == bJg or champ == bMid or champ == bAdc or champ == bSupp):
        pickCant = pickCant + 1


print("\nPickeada: ", pickCant, " Wins: ", winCant, "\n")
print("Winrate: ", (winCant/pickCant)*100, "\n")
