from difflib import SequenceMatcher

def similar(a,b):
    txt1 = open(a).readlines()
    txt2 = open(b).readlines()
    resultado = round(SequenceMatcher(None,txt1,txt2).ratio()*100,2)
    return resultado

def rptas():
    i = 0
    j = 0
    for i in range(0,len(archivos)):
        for j in range(0,len(archivos)):
            rpta = similar(archivos[i], archivos[j])
            porcentajes.append(rpta)


archivos = ["genomas/AY274119.txt",
            "genomas/AY278488.2.txt",
            "genomas/MN908947.txt",
            "genomas/MN988668.txt",
            "genomas/MN988669.txt"]

porcentajes =[]
rptas()

col= int(len(archivos))
fil = int(len(archivos))
matriz =[porcentajes[col*i : col*(i+1)] for i in range(fil)]
rptas()
for i in matriz:
    print(i)

