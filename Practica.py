import sys
from random import randint
from drawWordle import draw

#per obrir els fitxers corrrrrectament
def obrirfitxer(nom,RoW):
    f=None
    try:
        f=open(nom,RoW)
        return f
    except IOError:
        print("fitxer incorrecte")
        sys.exit(0)

#per crear llista de parelles a partir del fitxer mots.csv
def crearllpare(nomf):
    tta=obrirfitxer(nomf,"r")
    llpare=[]
    for linia in tta:
        llinia=linia.split("\n")
        llpare.append(llinia[0])
    tta.close()
    return llpare

#per escollir paraula a l'atzar
def parperpar():
    numberoparaula=randint(1,len(llpare))
    llnumpart=llpare[0].split(";")
    numpart=llnumpart[0]
    partot=str(int(numpart)+1)
    llpare[0]=str(partot)+";"
    llpara=llpare[numberoparaula].split(";")
    pescollida=llpara[0].upper()
    upara=llpara[1]
    while ((int(partot)-int(upara))<100) and (int(upara)>0):
        numberoparaula=randint(1,len(llpare)-1)
        llnumpart=llpare[0].split(";")
        numpart=llnumpart[0]
        llpara=llpare[numberoparaula].split(";")
        pescollida=llpara[0].upper()
        upara=llpara[1]
    llpare[numberoparaula]=str(llpara[0])+";"+str(partot)
    return pescollida 


#obrir fitxers jugadors
def dicjugcrear(djug,nomf):
    tta=obrirfitxer(nomf,"r")
    cap=tta.readline()
    for linia in tta:
        liniasepa=linia.split(";")
        llintjug=[]
        for i in range (1,(len(liniasepa)-1)):
            llintjug.append(liniasepa[i])
        djug[liniasepa[0]]=llintjug
    tta.close()
    return djug


#mostrar només llista dels noms dels jugadors
def moslljug(djug):
    cladicjug=list(djug.keys())
    cladicjug.sort()
    for nom in cladicjug:
        print(nom)

#crear diccionari jugadors
def dicju(djug):
    moslljug(djug)
    nom = input("Introdueix el teu nom: ")
    if nom not in djug:
        djug[nom]=[0,0,0,0,0,0,0]
    return nom
   
#iniciar el tauler
def initau():
    tauler= [[('', 0), ('', 0), ('', 0), ('', 0), ('', 0)],
             [('', 0), ('', 0), ('', 0), ('', 0), ('', 0)],
             [('', 0), ('', 0), ('', 0), ('', 0), ('', 0)],
             [('', 0), ('', 0), ('', 0), ('', 0), ('', 0)],
             [('', 0), ('', 0), ('', 0), ('', 0), ('', 0)],
             [('', 0), ('', 0), ('', 0), ('', 0), ('', 0)]]
    return tauler

#per jugar al joc
def jugar(pescollida):
    print(pescollida)
    #per desmontar la paraula escollida
    diclpesc={}
    for l in range(0,len(pescollida)): #Fa un diccionari on les lletres de la pesco són les claus i els valors són nombre de vegades que està la lletra, posció1, posició2,...
        if pescollida[l] not in diclpesc:
            llis=[]
            llis.append(1)
            llis.append(l)
            diclpesc[pescollida[l]]=llis
        else:
            diclpesc[pescollida[l]][0]+=1
            diclpesc[pescollida[l]].append(l)
    tauler=initau()
    draw(tauler)
    inten=0
    
    while inten<6:
        parinte=input("Entra un mot de 5 lletres:").upper()
        if len(parinte)!=5:
            print("Saps llegir? ")
        else:
            diclparinte={}
            for l in range(0,len(pescollida)): #Fa un diccionari on les lletres de la parinte són les claus i els valors són nombre de vegades que està la lletra, posció1, posició2,... 
                if parinte[l] not in diclparinte:
                    llis=[]
                    llis.append(1)
                    llis.append(l)
                    diclparinte[parinte[l]]=llis
                else:
                    diclparinte[parinte[l]][0]+=1
                    diclparinte[parinte[l]].append(l)
            tinte=tauler[inten]
            for k in range(0,len(parinte)):  #Mira si cada lletra de parinte està a pesco
                if parinte[k] not in diclpesc: #No està
                    tinte[k]=(parinte[k],0)
                elif parinte[k] in diclpesc: #Si que està
                    llpesco=[]
                    for t in range(1,len(diclpesc[parinte[k]])):
                        llpesco.append(diclpesc[parinte[k]][t])
                    llpari=[]
                    for t in range(1,len(diclparinte[parinte[k]])):
                        llpari.append(diclparinte[parinte[k]][t])
                    contpint=0
                    for p in llpari:
                        if p in llpesco:
                            tinte[p]=(parinte[p],2)
                            contpint+=1
                    for p in llpari:
                        if p not in llpesco:
                            if contpint<len(llpesco):
                                tinte[p]=(parinte[p],1)
                                contpint+=1
                            else:
                                tinte[p]=(parinte[p],0)
            tauler[inten]=tinte
            draw(tauler)
            if pescollida==parinte:
                return inten
            inten+=1
    inten=0
    return inten


#Per fer la partida
def partides(djug):
    dem=input("Vols fer una partida (S/N): ").upper()
    while dem=="S":
        nom=dicju(djug)
        pescollida=parperpar()
        tauler = initau
        inten = jugar(pescollida)
        djug[nom][inten]+=1
        dem=input("Vols fer una partida (S/N): ").upper()


#per reescriure el fitxer mots.csv
def actfitxermots(llpare,nomf):
    tta=open(nomf,"w") 
    for parella in llpare:
        fout.write(parella+"\n")
    tta.close()

#per actualitzar fitxer jugadors
def actfitxerjug(djug,nomf):
    tta=open(nomf,"w") 
    tta.write("Jugador;Perdudes;1 intent;2 intents;3 intents;4 intents;5 intents;6 intents\n")
    for nom in djug:
        tta.write(nom+';')
        for i in range(0,len(djug[nom])):
            if i==6:
                tta.write(str(djug[nom][i])+'\n')
            else:
                tta.write(str(djug[nom][i])+';')
    tta.close()

if __name__=="__main__":
    djug={}
    djug=dicjugcrear(djug,"jugadors.csv")
    llpare=crearllpare("mots.csv")
    partides(djug)
    #actfitxermots(llpare,"mots.csv")
    #actfitxerjug(djug,"jugadors.csv")
    
    #ranking(djug)
    print(llpare)
    print(parperpar())
    print(llpare)
    print(djug)
    print('tita')


    

    

























