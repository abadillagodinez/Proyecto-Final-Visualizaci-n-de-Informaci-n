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
    newCsv = "WinRate,Name,Health Points,HP Per Level,Mana Points,MP Per Level,Move Speed,Armor,Magic Resist,Attack Range,Attack Damage,Attack Speed\n"
    for i in dataChamps.index:
        champ = dataChamps["id"][i]
        hp = str(round(dataChamps["hp"][i],3))
        hpPerLevel = str(round(dataChamps["hpperlevel"][i],3))
        mp = str(round(dataChamps["mp"][i],3))
        mpPerLevel = str(round(dataChamps["mpperlevel"][i],3))
        ms = str(round(dataChamps["movespeed"][i],3))
        armor = str(round(dataChamps["armor"][i],3))
        spellblock = str(round(dataChamps["spellblock"][i],3))
        attackrange = str(round(dataChamps["attackrange"][i],3))
        ad = str(round(dataChamps["attackdamage"][i],3))
        attackspeed = str(round(dataChamps["attackspeed"][i],3))
        winRate = calculateWinRate(champ, dataMatches)
        line = str(round(winRate,2)) + "," + champ + "," + hp + "," + hpPerLevel + "," + mp + "," + mpPerLevel + "," + ms + "," + armor + "," + spellblock + "," + attackrange + "," + ad + "," + attackspeed + "\n"
        newCsv = newCsv + line
    file = open("./Data/champ_stats_w_winRate_FINAL.csv",'w')
    file.write(newCsv)
    file.close()

def calculateWinRate(champ, dataMatches):
    winCant = 0
    pickCant = 0

    for i in dataMatches.index:
        rTop = dataMatches["redtop"][i]
        rJg = dataMatches["redjungle"][i]
        rMid = dataMatches["redmid"][i]
        rAdc = dataMatches["redadc"][i]
        rSupp = dataMatches["redsupport"][i]
        bTop = dataMatches["bluetop"][i]
        bJg = dataMatches["bluejungle"][i]
        bMid = dataMatches["bluemid"][i]
        bAdc = dataMatches["blueadc"][i]
        bSupp = dataMatches["bluesupport"][i]
        win = dataMatches["result"][i]
        if (champ == rTop or champ == rJg or champ == rMid or champ == rAdc or champ == rSupp) and (win == 0):
            winCant = winCant + 1
        elif (champ == bTop or champ == bJg or champ == bMid or champ == bAdc or champ == bSupp) and (win == 1):
            winCant = winCant + 1

    for i in dataMatches.index:
        rTop = dataMatches["redtop"][i]
        rJg = dataMatches["redjungle"][i]
        rMid = dataMatches["redmid"][i]
        rAdc = dataMatches["redadc"][i]
        rSupp = dataMatches["redsupport"][i]
        bTop = dataMatches["bluetop"][i]
        bJg = dataMatches["bluejungle"][i]
        bMid = dataMatches["bluemid"][i]
        bAdc = dataMatches["blueadc"][i]
        bSupp = dataMatches["bluesupport"][i]
        win = dataMatches["result"][i]
        if (champ == rTop or champ == rJg or champ == rMid or champ == rAdc or champ == rSupp or champ == bTop or champ == bJg or champ == bMid or champ == bAdc or champ == bSupp):
            pickCant = pickCant + 1
    
    if(pickCant > 0):
        return ((winCant/pickCant)*100)
    else:
        return 0

def genCSVSpider():
    dataWorlds = pd.read_csv("./Data/Worlds 2020 Main Event - Team Stats - OraclesElixir.csv")
    newCsv = "Team,FB%,FT%,F3T%,HLD%,FD%,DRG%,ELD%,BN%\n"
    for i in dataWorlds.index:
        # get data from csv
        team = dataWorlds["Team"][i]
        fb = dataWorlds["FB%"][i]
        fb = fb[:-1] # remove %
        ft = dataWorlds["FT%"][i]
        ft = ft[:-1] # remove %
        f3t = dataWorlds["F3T%"][i]
        f3t = f3t[:-1] # remove %
        hld = dataWorlds["HLD%"][i]
        hld = hld[:-1] # remove %
        fd = dataWorlds["FD%"][i]
        fd = fd[:-1] # remove %
        drg = dataWorlds["DRG%"][i]
        drg = drg[:-1] # remove %
        eld = dataWorlds["ELD%"][i]
        eld = eld[:-1] # remove %
        bn = dataWorlds["BN%"][i]
        bn = bn[:-1] # remove %
        line = team + "," + fb + "," + ft + "," + f3t + "," + hld + "," + fd + "," + drg + "," + eld + "," + bn + "\n"
        newCsv = newCsv + line
    file = open("./Data/WorldsTeamStats_FINAL.csv",'w')
    file.write(newCsv)
    file.close()

genCSVParCoods()
genCSVSpider()