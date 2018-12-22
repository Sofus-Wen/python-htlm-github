import sys
I_alt = 0
Købe_2 = True

yes = {'yes','y', 'ye', "ja", "Ja", "j",''}
no = {'no','n', "nej", "nope"}

person = input("Skriv dit navn: ")
print("Hej", person, "!")

penge_nu = input("Hvor mange penge har du i banken: ")
print ("Du har", penge_nu, "Kr. i din bank")
penge_nu_1 = int(penge_nu)

penge = input("Det her er din bank, hvor meget vil du putte ind: ")
penge_1 = int(penge)
print ("Der er ", penge_nu_1+penge_1 , "Kr. i din bank nu", ".", sep="")

Købe = input("Vil du Købe noget: ")


def Købe_4():
    Købe_2 = input("Hvad vil du købe: ")
    print(Købe_2)
    Købe_3 = input("Vil du købe mere: ")
    print(Købe_3)

def Vi_ses_1():
    Vi_ses = input("Ok, Vi ses")
    print ("Ok, Vi ses")
choice = input().lower()
if choice in yes:
   print (Købe_4)
elif choice in no:
   print (Vi_ses_1)
else:
   sys.stdout.write("Please respond with 'yes' or 'no'")
