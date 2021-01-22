import pandas as pd



# imprime todas las composiciones donde el equipo rojo ganó
'''
for index in dataMatches.index:
    if(dataMatches["result"][index] == 1):
        print(dataMatches["redtop"][index], " ", dataMatches["redjungle"][index], " ", dataMatches["redmid"][index], " ", dataMatches["redadc"][index], " ", dataMatches["redsupport"][index])

redSuppts = dataMatches["redsupport"].tolist()
if 'Jax' in redSuppts:
    print("Yes, Jax was trolling")
'''

#función que crea el csv para el gráfico de barras paralelas
def genCSVParCoods():
    dataMatches = pd.read_csv("./Data/matches2020.csv")
    dataChamps = pd.read_csv("./Data/champion_stats.csv")
    newCsv = ""
    for index in dataChamps.index:
        champ = dataChamps["id"][index]
        winRate = calculateWinRate(champ, dataMatches)
        newCsv = newCsv + champ + "," + str(round(winRate,2)) + "\n"
    file = open("./Data/winRateByChamp.csv",'w')
    file.write(newCsv)
    file.close()

def calculateWinRate(champ, dataMatches):
    winCant = 0
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
        if (champ == rTop or champ == rJg or champ == rMid or champ == rAdc or champ == rSupp) and (win == 0):
            winCant = winCant + 1
        elif (champ == bTop or champ == bJg or champ == bMid or champ == bAdc or champ == bSupp) and (win == 1):
            winCant = winCant + 1

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
    
    if(pickCant > 0):
        return ((winCant/pickCant)*100)
    else:
        return 0

        
genCSVParCoods()