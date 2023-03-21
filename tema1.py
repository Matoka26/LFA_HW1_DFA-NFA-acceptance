with open("input1_example.txt") as f:
    n = int(f.readline())   #nr de stari
    start = f.readline().strip()    #starea initiala
    nrStariFinale = int(f.readline())   #nr stati finale
    stariFinale = [int(f.readline()) for i in range(nrStariFinale)] #lista stari finale

#datele vor fi citite ca o matrice de adiacenta
#sunt salvate intr-un dictionar,key-ul este starea,valoarea este o lista cu listele de litere care duc catre fiecare nod
#completat cu '-' unde nu exista drum
    matrix = {}
    for i in range(n):
        matrix[i] = [['-']]*n

    aux = 0
    while aux != "":
        aux = f.readline().strip()
        if aux == "":
            break
        aux2 = int(f.readline().strip())
        aux3 = f.readline().strip()
        matrix[int(aux)][aux2] = aux3.split(',')

cuvant = input("cuvant: ")
if cuvant == ' ':
    if int(start) in stariFinale:
        print("Acceptat")
    else:
        print("Neacceptat")
else:
    print("1.Afisarea explicita cu sagetute\n2.Scrierea cu configuratie\n")
    metoda = int(input(""))     #citeste metoda de afisare aleasa
    if metoda == 1:
        stariActuale = int(start)

        drumuriBune = [[int(start)]]       #vom avea o lista de liste care reprezinta posibile drumuri inca valide
        for litera in cuvant:
            noileDrumuri = []
            for posibilDrum in drumuriBune:
                for i in range(n):
                    if litera in matrix[int(posibilDrum[-1])][i]:   #daca pe linia pe care ne aflam cu starea avem drum prin litera curenta catre
                        copieLista = posibilDrum.copy()             #o alta stare o salvam,iar daca avem catre mai multe vom avea o copie cu ultimul
                        copieLista.append(i)                        #elemente diferit
                        noileDrumuri.append(copieLista)
                        copieLista = ""
            drumuriBune = noileDrumuri  #la fiecare litera vom considera noua lista de drumuri potential valide
        check = 0
        if len(drumuriBune) != 0:                   #daca nu avem niciun drum potential valid inseamna ca s-a dat abort
            for drumulet in drumuriBune:            #daca avem totusi drum le afisam daca au ultimul element o stare finala,altfel drumul este invalid
                if drumulet[-1] in stariFinale:     #daca nu avem niciun drum valid atunci afisam "invalid"
                    check = 1
                    for i in range(len(drumulet)):
                        if i != len(drumulet)-1:
                            print(f'({drumulet[i]})-->',end="")
                        else:
                            print(f'(({drumulet[i]}))')
        else:
            print("~Abort~")
        if check == 0:
            print("invalid")
        else:
            print("acceptat")
    else:
        stariActuale = set(start)           #tinem starile curente intr-un set pentru a elimina duplicatele in cazul unui NFA
        print(f'({stariActuale},{cuvant})|- ', end="")
        k = 0
        j = 0
        for litera in cuvant:
            j += 1
            noiStariActuale = set()
            for stare in stariActuale:      #salvam intr-un nou set noile stari care duc la pasul urmator
                for i in range(0, n):
                    if litera in matrix[int(stare)][i]:
                        noiStariActuale.add(i)
            stariActuale = noiStariActuale  #actualizam setul cu noile stari gasite
            if len(noiStariActuale) == 0:       #daca nu avme nicio noua stare curenta avem abort
                print("~Abort~")
                print("invalid")
                k = 1
                break
            if j == len(cuvant):        #cand am terminat si ultimul caracter afisam starile actuale la care am ajuns si caracterul lambda
                print(f'({stariActuale},{chr(955)})|- ', end="")
            else:
                print(f'({stariActuale},{cuvant[j:]})|- ', end="")

        j = 0
        if k == 0:
            for i in stariActuale:      #daca vreo stare gasita e finala afisam "acceptat" else "invalid"
                if i in stariFinale:
                    print("acceptat")
                    j = 1
                    break
            if j == 0:
                print("invalid")
