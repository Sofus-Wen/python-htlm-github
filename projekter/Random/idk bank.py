import sys
import random


I_alt = 0
Købe_2 = True

yes = {'yes', 'y', 'ye', "ja", "Ja", "j", ''}
no = {'no', 'n', "nej", "nope"}

person = input("Skriv dit navn: ")
print("Hej", person, "!")

penge_nu = input("Hvor mange penge har du i banken: ")
print("Du har", penge_nu, "Kr. i din bank")
penge_nu_1 = int(penge_nu)

penge = input("Det her er din bank, hvor meget vil du putte ind: ")
penge_1 = int(penge)
print("Der er ", penge_nu_1 + penge_1, "Kr. i din bank nu", ".", sep="")

Købe = input("Vil du Købe noget: ")


def Købe_4():
    Købe_2 = input("Hvad vil du købe: ")
    print(Købe_2)
    Købe_5 = int(Købe_2)
    pris_11 = input(random.randint(1, 999999))
    print("En/Et", Købe_5, "koster ", pris_11, "Kr.")
    Købe_3 = input("Vil du købe mere: ")
    print(Købe_3)


def Vi_ses_1():
    Vi_ses = input("Ok, Vi ses")
    print("Ok, Vi ses")
    exit()


choice = input().lower()
if choice in yes:
    Købe_4()
elif choice in no:
    Vi_ses_1()
else:
    sys.stdout.write("Prov at skrive ja eller nej'")

