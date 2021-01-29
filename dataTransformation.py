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

def genCSVBarras():
    dataMatches = pd.read_csv("./Data/matches2020.csv")
    dataChamps = pd.read_csv("./Data/champion_stats.csv")
    newCsv = "Posicion,"
    indexes = len(dataChamps.index)-1
    i = 0
    while(i < indexes):
        champ = dataChamps["id"][i]
        newCsv += champ + ","
        i += 1
    newCsv += dataChamps["id"][indexes] + "\n"

    i = 0
    newCsv += "Top,"
    while(i < indexes):
        champ = dataChamps["id"][i]
        winRateOnTop = calculateWinRateTop(champ,dataMatches)
        newCsv += str(round(winRateOnTop,3)) + ","
        i += 1
    lastWRTop = calculateWinRateTop(dataChamps["id"][indexes], dataMatches)
    newCsv += str(round(lastWRTop,3)) + "\n"

    i = 0
    newCsv += "Jungle,"
    while(i < indexes):
        champ = dataChamps["id"][i]
        winRateOnTop = calculateWinRateJungle(champ,dataMatches)
        newCsv += str(round(winRateOnTop,3)) + ","
        i += 1
    lastWRTop = calculateWinRateJungle(dataChamps["id"][indexes], dataMatches)
    newCsv += str(round(lastWRTop,3)) + "\n"

    i = 0
    newCsv += "Mid,"
    while(i < indexes):
        champ = dataChamps["id"][i]
        winRateOnTop = calculateWinRateMid(champ,dataMatches)
        newCsv += str(round(winRateOnTop,3)) + ","
        i += 1
    lastWRTop = calculateWinRateMid(dataChamps["id"][indexes], dataMatches)
    newCsv += str(round(lastWRTop,3)) + "\n"

    i = 0
    newCsv += "Adc,"
    while(i < indexes):
        champ = dataChamps["id"][i]
        winRateOnTop = calculateWinRateAdc(champ,dataMatches)
        newCsv += str(round(winRateOnTop,3)) + ","
        i += 1
    lastWRTop = calculateWinRateAdc(dataChamps["id"][indexes], dataMatches)
    newCsv += str(round(lastWRTop,3)) + "\n"

    i = 0
    newCsv += "Support,"
    while(i < indexes):
        champ = dataChamps["id"][i]
        winRateOnTop = calculateWinRateSupp(champ,dataMatches)
        newCsv += str(round(winRateOnTop,3)) + ","
        i += 1
    lastWRTop = calculateWinRateSupp(dataChamps["id"][indexes], dataMatches)
    newCsv += str(round(lastWRTop,3))
    print(newCsv)
     
def calculateWinRateTop(champ, dataMatches):
    pickCant = 0
    winCant = 0
    for i in dataMatches.index:
        rTop = dataMatches["redtop"][i]
        bTop = dataMatches["bluetop"][i]
        win = dataMatches["result"][i]
        if (champ == rTop  and win == 0) or (champ == bTop and win == 1):
            winCant = winCant + 1
    
    for i in dataMatches.index:
        rTop = dataMatches["redtop"][i]
        bTop = dataMatches["bluetop"][i]
        if (champ == rTop or champ == bTop):
            pickCant = pickCant + 1
    
    if(pickCant > 0):
        return ((winCant/pickCant)*100)
    else:
        return 0

def calculateWinRateJungle(champ, dataMatches):
    pickCant = 0
    winCant = 0
    for i in dataMatches.index:
        rTop = dataMatches["redjungle"][i]
        bTop = dataMatches["bluejungle"][i]
        win = dataMatches["result"][i]
        if (champ == rTop  and win == 0) or (champ == bTop and win == 1):
            winCant = winCant + 1
    
    for i in dataMatches.index:
        rTop = dataMatches["redjungle"][i]
        bTop = dataMatches["bluejungle"][i]
        if (champ == rTop or champ == bTop):
            pickCant = pickCant + 1
    
    if(pickCant > 0):
        return ((winCant/pickCant)*100)
    else:
        return 0

def calculateWinRateMid(champ, dataMatches):
    pickCant = 0
    winCant = 0
    for i in dataMatches.index:
        rTop = dataMatches["redmid"][i]
        bTop = dataMatches["bluemid"][i]
        win = dataMatches["result"][i]
        if (champ == rTop  and win == 0) or (champ == bTop and win == 1):
            winCant = winCant + 1
    
    for i in dataMatches.index:
        rTop = dataMatches["redmid"][i]
        bTop = dataMatches["bluemid"][i]
        if (champ == rTop or champ == bTop):
            pickCant = pickCant + 1
    
    if(pickCant > 0):
        return ((winCant/pickCant)*100)
    else:
        return 0
    
def calculateWinRateAdc(champ, dataMatches):
    pickCant = 0
    winCant = 0
    for i in dataMatches.index:
        rTop = dataMatches["redadc"][i]
        bTop = dataMatches["blueadc"][i]
        win = dataMatches["result"][i]
        if (champ == rTop  and win == 0) or (champ == bTop and win == 1):
            winCant = winCant + 1
    
    for i in dataMatches.index:
        rTop = dataMatches["redadc"][i]
        bTop = dataMatches["blueadc"][i]
        if (champ == rTop or champ == bTop):
            pickCant = pickCant + 1
    
    if(pickCant > 0):
        return ((winCant/pickCant)*100)
    else:
        return 0

def calculateWinRateSupp(champ, dataMatches):
    pickCant = 0
    winCant = 0
    for i in dataMatches.index:
        rTop = dataMatches["redsupport"][i]
        bTop = dataMatches["bluesupport"][i]
        win = dataMatches["result"][i]
        if (champ == rTop  and win == 0) or (champ == bTop and win == 1):
            winCant = winCant + 1
    
    for i in dataMatches.index:
        rTop = dataMatches["redsupport"][i]
        bTop = dataMatches["bluesupport"][i]
        if (champ == rTop or champ == bTop):
            pickCant = pickCant + 1
    
    if(pickCant > 0):
        return ((winCant/pickCant)*100)
    else:
        return 0

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

def getAllTeamsRedAndBlue():
    dataMatches = pd.read_csv("./Data/matches2020.csv")
    redTeams = []
    blueTeams = []
    for i in dataMatches.index:
        redTeams += [dataMatches["redteam"][i]]
        blueTeams += [dataMatches["blueteam"][i]]
    uniqueReds = []
    uniqueBlues = []
    for team in redTeams:
        if team not in uniqueReds:
            uniqueReds += [team]
    for team in blueTeams:
        if team not in uniqueBlues:
            uniqueBlues += [team]
    return uniqueBlues, uniqueReds    

def getMostTopPlayedByRTeam(redTeam):
    dataMatches = pd.read_csv("./Data/matches2020.csv")
    champsPlayed = []
    for i in dataMatches.index:
        if dataMatches["redteam"][i] == redTeam:
            champsPlayed += [dataMatches["redtop"][i]]
    return (most_frequent(champsPlayed))

def getMostJunglePlayedByRTeam(redTeam):
    dataMatches = pd.read_csv("./Data/matches2020.csv")
    champsPlayed = []
    for i in dataMatches.index:
        if dataMatches["redteam"][i] == redTeam:
            champsPlayed += [dataMatches["redjungle"][i]]
    return (most_frequent(champsPlayed))

def getMostMidPlayedByRTeam(redTeam):
    dataMatches = pd.read_csv("./Data/matches2020.csv")
    champsPlayed = []
    for i in dataMatches.index:
        if dataMatches["redteam"][i] == redTeam:
            champsPlayed += [dataMatches["redmid"][i]]
    return (most_frequent(champsPlayed))

def getMostAdcPlayedByRTeam(redTeam):
    dataMatches = pd.read_csv("./Data/matches2020.csv")
    champsPlayed = []
    for i in dataMatches.index:
        if dataMatches["redteam"][i] == redTeam:
            champsPlayed += [dataMatches["redadc"][i]]
    return (most_frequent(champsPlayed))

def getMostSuppPlayedByRTeam(redTeam):
    dataMatches = pd.read_csv("./Data/matches2020.csv")
    champsPlayed = []
    for i in dataMatches.index:
        if dataMatches["redteam"][i] == redTeam:
            champsPlayed += [dataMatches["redsupport"][i]]
    return (most_frequent(champsPlayed))

def getMostTopPlayedByBTeam(blueTeam):
    dataMatches = pd.read_csv("./Data/matches2020.csv")
    champsPlayed = []
    for i in dataMatches.index:
        if dataMatches["blueteam"][i] == blueTeam:
            champsPlayed += [dataMatches["redtop"][i]]
    return (most_frequent(champsPlayed))

def getMostJunglePlayedByBTeam(blueTeam):
    dataMatches = pd.read_csv("./Data/matches2020.csv")
    champsPlayed = []
    for i in dataMatches.index:
        if dataMatches["blueteam"][i] == blueTeam:
            champsPlayed += [dataMatches["bluejungle"][i]]
    return (most_frequent(champsPlayed))

def getMostMidPlayedByBTeam(blueTeam):
    dataMatches = pd.read_csv("./Data/matches2020.csv")
    champsPlayed = []
    for i in dataMatches.index:
        if dataMatches["blueteam"][i] == blueTeam:
            champsPlayed += [dataMatches["bluemid"][i]]
    return (most_frequent(champsPlayed))

def getMostAdcPlayedByBTeam(blueTeam):
    dataMatches = pd.read_csv("./Data/matches2020.csv")
    champsPlayed = []
    for i in dataMatches.index:
        if dataMatches["blueteam"][i] == blueTeam:
            champsPlayed += [dataMatches["blueadc"][i]]
    return (most_frequent(champsPlayed))

def getMostSuppPlayedByBTeam(blueTeam):
    dataMatches = pd.read_csv("./Data/matches2020.csv")
    champsPlayed = []
    for i in dataMatches.index:
        if dataMatches["blueteam"][i] == blueTeam:
            champsPlayed += [dataMatches["bluesupport"][i]]
    return (most_frequent(champsPlayed))

def genCSVMap():
    blueTeams, redTeams = getAllTeamsRedAndBlue()
    # genera csv rojos
    newCsv = "Team,Top,Jungle,Mid,Adc,Support\n"
  
    for team in blueTeams:
        redTop = getMostTopPlayedByRTeam(team)
        redJg = getMostJunglePlayedByRTeam(team)
        redMid = getMostMidPlayedByRTeam(team)
        redAdc = getMostAdcPlayedByRTeam(team)
        redSup = getMostSuppPlayedByRTeam(team)
        newCsv += team + "," + redTop + "," + redJg + "," + redMid + "," + redAdc + "," + redSup + "\n"
    
    print(newCsv)



def most_frequent(List): 
    return max(set(List), key = List.count) 

# genCSVParCoods()
# genCSVSpider()
# getAllTeamsRed()
# print(getMostAdcPlayedByBTeam("T1"))
# genCSVMap()
genCSVBarras()
