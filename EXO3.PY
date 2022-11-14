import EXO1
import EXO2
while True:
    print("****************Menu principale**************")
    print("tapez 1.Exercice1:")
    print("tapez 2.Exercice2:")
    print("tapez 3.quitter:")
    choix=input()

    if(choix=="1"):
        print("***************Exercice1******************")
        N= input("Donnez la valeur de N :")


        try :
            N= int(N)
            while True :
                print("tapez 1.affiche L:")
                print("tapez 2.calculer R:")
                print("tapez 3.retour au menu principal:")
                choix_2= input()
                if(choix_2=="1"):
                    print(EXO1.L(N))
                elif(choix_2=="2"):
                    print(EXO1.R(N))
                elif(choix_2=="3"):
                    break
                else:
                    print("choix invalide")
        except:
            print("Donnée invalide")
    
    elif(choix=="2"):
        print("*************Exercice2********************")
        print("Donnez la valeur de n:")
        n=input()
        print("Donnez la valeur s:")
        s=input()
        try:
            n= int(n)
            s= int(s)
            while True:
                dataTrans= EXO2.DataTrans(n,s)
                print("tapez 1.afficher la liste D:")
                print("tapez 2.afficher Les min et les max:")
                print("tapez 3.afficher le min global:")
                print("tapez 4.afficher le max global:")
                print("tapez 5.calculer D':")
                print("tapez 6.retour au menu principal:")
                
                choix_3= input()
                if(choix_3=="1"):
                    print(dataTrans.getD())
                elif(choix_3=="2"):
                    print(dataTrans.getMinMax())
                elif(choix_3=="3"):
                    print(dataTrans.minGlobal())
                elif(choix_3=="4"):
                    print(dataTrans.maxGlobal())
                elif(choix_3=="5"):
                    print(dataTrans.dPrime())
                elif(choix_3=="6"):
                    break
                else:
                    print("choix invalide")
        except:
            print("Donnee invalide")
    elif(choix=="3"):
        break
    else:
        print("choix invalide")
print("fin....")
                



