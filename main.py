#fuggvenyek

def sorozat(nn):
    if nn==1:
        return 2
    
    elif nn==2:
        return 3
    
    elif nn==3:
        return 5
    
    else:
        return 2*sorozat(nn-1)+3*sorozat(nn-2)-sorozat(nn-3)
    
#0

print("Sorozatok")

#1

adat=input("Kérem a sorozat számait ';' vel elválasztva: ")
adatok=adat.split(";")
a=float(adatok[0].replace(",","."))
b=float(adatok[1].replace(",","."))

if a>b:
    a,b=b,a

#2

sorjo=[]

n=1

while True:
    elem=sorozat(n)
    if elem>=a and elem<=b:
        sorjo.append(elem)

    if elem>b:
        break

    n+=1

#3
tempstr=[]

for item in sorjo:
    tempstr.append(str(item))

kiiras= " ; ".join(tempstr)

print(kiiras)