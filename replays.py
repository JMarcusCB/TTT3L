saves = []

def readLine(totSaves):
    global saves
    lines = 0
    gamenote = ""
    try:
        with open("save.txt", "r") as file:
            for row in file:
                if row != "\n":
                    note = row
                    gamenote = ""
                    for i in note:
                        if i != "\n":
                            gamenote += i

                    saves.append(gamenote)

                    lines += 1
    except FileNotFoundError:
        with open("save.txt", "w") as file:
            for i in range(totSaves):
                file.write("free")
                file.write(f"\n")
            readLine(totSaves)

def updateFile():
    global saves
    lines = len(saves)
    with open("save.txt", "w") as file:
        for i in range(lines):
            file.write(saves[i])
            file.write(f"\n")

def fileToGamenote(index):
    global saves
    index = index -1
    for i in range(len(saves)):
        if index <= len(saves):
            if i == index:
                return saves[index]

def saveFile(index, gamenote):
    index = index -1
    global saves
    filenote = ""
    for bx in gamenote:
        jogada = bx.casa.index
        filenote += str(jogada)

    for i in range(len(saves)):
        if i == index:
            saves[index] = str(filenote)

    updateFile()

def removeGamenote(index):
    global saves
    index = index -1
    for i in range(len(saves)):
        if i == index:
            saves[index] = "free"
    
    with open("save.txt", "w") as file:
        file.write("")

    updateFile()


    


    