import random

def chooseNumbers(howMany):
    order = 1
    for order in range(1, int(howMany)):
        choosenNumber = random.randint(1,99)
        if 40 < choosenNumber < 60:
            print(order,". cislo, ktere je", choosenNumber ,"se veslo do intervalu.")
        order = order + 1

def printHead():
    print("Prvni domaci ukol. Priklad s pouzitim volani funkci, pouziti cyklu a podminky.")
    print("Tento script vybere zadany pocet nahodnych cisel v rozmezi 1 - 100 a vypise ty, ktere budou v intervalu 40 - 60.")

def readInput():
    howMany = input("Zadej pocet cisel k posouzeni: ")
    if howMany.isdigit():
        chooseNumbers(howMany)
    else:
        print("Prosím, zadejte číslo!")
        readInput()

def wantContinue():
    answer = input("Přejete si znovu zadat počet čísel? y/n\n")
    if answer == "y":
        readInput()
    elif answer == "n":
        print("Děkujeme za požití našeho skvělého sw. Nashledanou.")
        exit()
    else:
        wantContinue()
    wantContinue()

def __main__():
    printHead()
    readInput()
    wantContinue()
__main__()